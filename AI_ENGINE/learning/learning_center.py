"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Learning Center
==========================================================
"""

import pandas as pd

from pathlib import Path



from AI_ENGINE.learning import (
    PerformanceHistory,
    StatisticsEngine,
    WeightLearner,
)


class LearningCenter:

    def __init__(

        self,

        history_file,

    ):

        self.history_file = Path(history_file)
        
        
        
        
        
    #---------------------------------------------

    def save_weight(

        self,

        weight,

    ):

        df = pd.DataFrame(

            [

                {

                    "Factor": "money",

                    "Weight": weight.money,

                },

                {

                    "Factor": "liquidity",

                    "Weight": weight.liquidity,

                },

                {

                    "Factor": "trend",

                    "Weight": weight.trend,

                },

                {

                    "Factor": "momentum",

                    "Weight": weight.momentum,

                },

                {

                    "Factor": "institution",

                    "Weight": weight.institution,

                },

                {

                    "Factor": "trade",

                    "Weight": weight.trade,

                },

                {

                    "Factor": "revenue",

                    "Weight": weight.revenue,

                },

                {

                    "Factor": "theme",

                    "Weight": weight.theme,

                },

                {

                    "Factor": "priority",

                    "Weight": weight.priority,

                },

            ]

        )

        output = self.history_file.parent / "AI_WEIGHT.xlsx"

        df.to_excel(

            output,

            index=False,

        )

        return output
    
    
    # -------------------------------------------------
    
    def run(self):

        #
        # 讀取歷史
        #

        history = PerformanceHistory(

            self.history_file

        )

        records = history.load()

        #
        # Statistics
        #

        statistics = StatisticsEngine(

            records,

        )

        factor_df = statistics.factor_statistics()

        #
        # Weight Learn
        #

        learner = WeightLearner()

        weight = learner.learn(

            factor_df,

        )
        
        self.save_weight(

            weight

        )

        return (

            weight,

            factor_df,

            statistics.summary(),

        )
    
    
    
    
    

  