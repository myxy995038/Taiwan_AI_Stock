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

            "成交值分數":"money",

            "流動性分數":"liquidity",

            "趨勢分數":"trend",

            "動能分數":"momentum",

            "法人共振分數":"institution",

            "RR加權分數":"trade",

            "營收分數":"revenue",

            "題材":"theme",

            "Priority":"priority",

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