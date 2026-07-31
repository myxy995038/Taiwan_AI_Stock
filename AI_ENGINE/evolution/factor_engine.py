import pandas as pd


class FactorEngine:

    def evaluate(self, history):

        if history.empty:
            return pd.DataFrame()

        result = []

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

        for factor in factor_list:

            if factor not in history.columns:
                continue

            result.append({

                "Factor": factor,

                "Average": history[factor].mean(),

                "WinRate":
                    (history["success"] == True).mean(),

                "AvgReturn":
                    history["return_rate"].mean(),

            })

        return pd.DataFrame(result)