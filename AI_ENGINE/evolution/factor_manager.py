import pandas as pd
from AI_ENGINE.evolution.factor_history import FactorHistory
from AI_ENGINE.evolution.factor_engine import FactorEngine
from AI_ENGINE.learning.weight_learner import WeightLearner
from AI_ENGINE.evolution.factor_status import FactorStatus


class FactorManager:

    def __init__(self, history_file):
        self.history = FactorHistory(history_file)
        self.engine = FactorEngine()
        self.learner = WeightLearner()
        self.status = FactorStatus()

    def run(self):
        history_df = self.history.load()
        factor_df = self.engine.evaluate(history_df)
        status_df = self.status.load()

        if factor_df.empty:
            return None

        weight = self.learner.learn(factor_df)

        # ==========================
        # 寫回 AI_WEIGHT.xlsx
        # ==========================
        output = self.history.file.parent / "AI_WEIGHT.xlsx"

        weight_rows = []

        mapping = {
            "money_score": weight.money,
            "liquidity_score": weight.liquidity,
            "trend_score": weight.trend,
            "momentum_score": weight.momentum,
            "institution_score": weight.institution,
            "trade_score": weight.trade,
            "revenue_score": weight.revenue,
            "theme_score": weight.theme,
            "priority_score": weight.priority,
        }

        # 修正後的 for 迴圈區塊 (正確縮排)
        for _, row in factor_df.iterrows():
            factor = row["Factor"]
            enabled = row["Enabled"]

            # 1. 更新狀態表 (status_df)
            old = status_df[status_df["Factor"] == factor]

            if len(old) == 0:
                status_df.loc[len(status_df)] = {
                    "Factor": factor,
                    "Enabled": enabled,
                    "DisableCount": 0,
                    "ResurrectionCount": 0,
                    "LastStatus": "Active" if enabled else "Disabled",
                }
            else:
                idx = old.index[0]
                old_enabled = bool(status_df.loc[idx, "Enabled"])

                if old_enabled and not enabled:
                    status_df.loc[idx, "DisableCount"] += 1
                    status_df.loc[idx, "LastStatus"] = "Disabled"
                elif (not old_enabled) and enabled:
                    status_df.loc[idx, "ResurrectionCount"] += 1
                    status_df.loc[idx, "LastStatus"] = "Resurrected"

                status_df.loc[idx, "Enabled"] = enabled

            # 2. 收集權重資料
            if factor not in mapping:
                continue

            weight_rows.append({
                "Factor": factor,
                "Weight": mapping[factor],
                "Enabled": row.get("Enabled", True),
            })

        # 儲存 Excel 與 狀態檔案
        pd.DataFrame(weight_rows).to_excel(
            output,
            index=False,
        )

        self.status.save(status_df)

        return weight