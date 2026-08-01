"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Feature Importance Engine
==========================================================
"""

import pandas as pd
from pathlib import Path


class FeatureImportance:

    def __init__(self, history_file):

        self.history_file = Path(history_file)

    # -------------------------------------------------

    def run(self):

        if not self.history_file.exists():

            print("⚠ 找不到績效歷史")

            return pd.DataFrame()

        df = pd.read_excel(self.history_file)

        if len(df) == 0:

            return pd.DataFrame()

        success = df[df["success"] == True]
        failure = df[df["success"] == False]

        factor_list = [

            "money_score",
            "liquidity_score",
            "trend_score",
            "momentum_score",
            "institution_score",
            "trade_score",
            "revenue_score",
            "theme_score",
            "priority_score",

        ]

        rows = []

        total_power = 0

        for factor in factor_list:

            if factor not in df.columns:
                continue

            s = success[factor].mean() if len(success) else 0
            f = failure[factor].mean() if len(failure) else 0

            power = abs(s - f)

            total_power += power

            rows.append({

                "Factor": factor,

                "SuccessMean": round(s, 2),

                "FailureMean": round(f, 2),

                "Power": round(power, 2),

            })

        result = pd.DataFrame(rows)

        if total_power == 0:

            result["Importance"] = 0

        else:

            result["Importance"] = (
                result["Power"] / total_power * 100
            ).round(2)

        result = result.sort_values(
            "Importance",
            ascending=False,
        ).reset_index(drop=True)

        result.insert(0, "Rank", result.index + 1)

        output = (
            self.history_file.parent /
            "FeatureImportance.xlsx"
        )

        result.to_excel(
            output,
            index=False,
        )

        print("✅ 已更新 FeatureImportance.xlsx")

        return result