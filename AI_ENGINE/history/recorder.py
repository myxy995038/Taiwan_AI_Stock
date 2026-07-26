"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

History Recorder
==========================================================
"""

from AI_ENGINE.learning import (
    LearningRecord,
    PerformanceHistory,
)


class HistoryRecorder:

    def __init__(

        self,

        history_file,

    ):

        self.history = PerformanceHistory(

            history_file

        )

        self.history.load()

    # -------------------------------------------------

    def record(

        self,

        stock_id,

        stock_name,

        score,

        feature,

        return_rate,

        holding_days,

        success,

        comment="",

    ):

        record = LearningRecord(

            stock_id=stock_id,

            stock_name=stock_name,

            date="",

            total_score=score.total,

            money_score=score.money,

            liquidity_score=score.liquidity,

            trend_score=score.trend,

            momentum_score=score.momentum,

            institution_score=score.institution,

            trade_score=score.trade,

            revenue_score=score.revenue,

            theme_score=score.theme,

            priority_score=score.priority,

            rr=feature.trade.rr,

            return_rate=return_rate,

            holding_days=holding_days,

            success=success,

            theme=feature.theme.primary,

            comment=comment,

        )

        self.history.add(

            record

        )

        self.history.save()

        return record