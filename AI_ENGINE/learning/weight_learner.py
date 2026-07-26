"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Weight Learner V2
==========================================================
"""

from AI_ENGINE.score import AIWeight


class WeightLearner:

    def __init__(self):

        self.weight = AIWeight()

    # -------------------------------------------------

    def calc_weight(

        self,

        factor_power,

        success_rate,

        avg_return,

        samples,

    ):

        #
        # 基本倍率
        #

        weight = 1.0

        #
        # Factor Power
        #

        if factor_power >= 20:

            weight += 0.20

        elif factor_power >= 10:

            weight += 0.10

        elif factor_power >= 5:

            weight += 0.05

        #
        # 勝率
        #

        if success_rate >= 0.70:

            weight += 0.10

        elif success_rate >= 0.60:

            weight += 0.05

        #
        # 平均報酬
        #

        if avg_return >= 8:

            weight += 0.10

        elif avg_return >= 5:

            weight += 0.05

        #
        # 樣本數
        #

        if samples >= 500:

            weight += 0.10

        elif samples >= 100:

            weight += 0.05

        #
        # 上限
        #

        weight = min(

            weight,

            1.50,

        )

        return round(

            weight,

            2,

        )

    # -------------------------------------------------

    def learn(

        self,

        factor_df,

    ):

        mapping = {

            "money_score": "money",

            "liquidity_score": "liquidity",

            "trend_score": "trend",

            "momentum_score": "momentum",

            "institution_score": "institution",

            "trade_score": "trade",

            "revenue_score": "revenue",

            "theme_score": "theme",

            "priority_score": "priority",

        }

        for _, row in factor_df.iterrows():

            factor = row["Factor"]

            if factor not in mapping:

                continue

            value = self.calc_weight(

                row["FactorPower"],

                row["SuccessRate"],

                row["AvgReturn"],

                row["Samples"],

            )

            setattr(

                self.weight,

                mapping[factor],

                value,

            )

        return self.weight