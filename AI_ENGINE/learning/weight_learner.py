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

            setattr(

                self.weight,

                mapping[factor],

                row["WeightSuggestion"]
        
            )

        return self.weight