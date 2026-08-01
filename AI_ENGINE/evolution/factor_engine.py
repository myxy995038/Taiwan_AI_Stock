import pandas as pd


class FactorEngine:

    def evaluate(self, history):

        if history.empty:
            return pd.DataFrame()

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

        success = history[history["success"] == True]
        failure = history[history["success"] == False]

        for factor in factor_list:

            if factor not in history.columns:
                continue

            avg = history[factor].mean()

            success_avg = success[factor].mean() if len(success) else 0
            failure_avg = failure[factor].mean() if len(failure) else 0

            factor_power = success_avg - failure_avg
            
            # ==========================================
            # AI Factor Evolution
            # ==========================================

            weight = 1.00

            # FactorPower
            if factor_power >= 20:
                weight += 0.20
            elif factor_power >= 10:
                weight += 0.10
            elif factor_power >= 5:
                weight += 0.05

            # 勝率
            success_rate = len(success) / len(history)

            if success_rate >= 0.75:
                weight += 0.15
            elif success_rate >= 0.65:
                weight += 0.10
            elif success_rate >= 0.55:
                weight += 0.05

            # 平均報酬
            avg_return = history["return_rate"].mean()

            if avg_return >= 10:
                weight += 0.15
            elif avg_return >= 5:
                weight += 0.10
            elif avg_return >= 2:
                weight += 0.05

            # 樣本數可信度
            samples = len(history)

            if samples >= 500:
                weight += 0.10
            elif samples >= 100:
                weight += 0.05

            # 上限
            weight = min(weight, 1.50)
            
            enabled = (
                samples < 100
                or (
                    factor_power > 0
                    and success_rate >= 0.50
                )
            )

            # -----------------------------
            # Resurrection（復活）
            # -----------------------------
            if (
                not enabled
                and samples >= 300
                and factor_power >= 5
                and success_rate >= 0.60
            ):
                enabled = True
            
            
            

            rows.append({
            
            
                    "Factor": factor,

                    "Samples": samples,

                    "Average": round(avg, 2),

                    "SuccessAvg": round(success_avg, 2),

                    "FailureAvg": round(failure_avg, 2),

                    "FactorPower": round(factor_power, 2),

                    "SuccessRate": round(success_rate, 4),

                    "AvgReturn": round(avg_return, 2),

                    "WeightSuggestion": round(weight, 2),

                    "Enabled": enabled,

    
            })

        return pd.DataFrame(rows)