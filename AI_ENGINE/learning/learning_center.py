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

from AI_ENGINE.learning.models import LearningRecord

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
    
   

    def append_today(
        self,
        result_df,
    ):

        history = PerformanceHistory(
            self.history_file
        )

        history.load()

        for _, row in result_df.iterrows():

            record = LearningRecord(

                stock_id=str(row["代號"]),
                stock_name=row["名稱"],
                date=str(pd.Timestamp.today().date()),

                total_score=row["總分"],

                money_score=row["成交值分數"],
                liquidity_score=row["流動性分數"],
                trend_score=row["趨勢分數"],
                momentum_score=row["動能分數"],
                institution_score=row["法人共振分數"],
                trade_score=row["RR加權分數"],
                revenue_score=row["營收分數"],
                theme_score=0,
                priority_score=row["Priority"],

                rr=row["RR數值"],

                return_rate=row.get("漲跌%", 0),

                holding_days=0,

                success=row.get("漲跌%", 0) > 0,

                theme=row["題材"],

                comment=row["AI評論"],

                quality=row["AI品質(總分)"],

                action=row["AI建議"],

                entry_timing=row["AI進場時機"],

            )

            history.add(record)

        history.save()
    
    
    # -------------------------------------------------    
             
        
    def run(
        self,
    ):    

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
    