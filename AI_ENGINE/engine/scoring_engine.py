"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Scoring Engine V3
==========================================================
"""

from AI_ENGINE.score import (
    ScoreResult,
    AIWeight,
)

from AI_ENGINE.learning.weight_loader import WeightLoader

from AI_ENGINE.constants import (
    THEME_SCORE,
)


class ScoringEngine:

    def __init__(
        self,
        weight=None,
        auto_load=True,
    ):
        if auto_load:
            loader = WeightLoader()
            self.weight = loader.load()
        else:
            if weight is None:
                weight = AIWeight()
            self.weight = weight

    # -------------------------------------------------

    def score_market(
        self,
        feature,
        score,
    ):
        score.money = (
            feature.market.money *
            self.weight.money
        )
        score.liquidity = (
            feature.market.liquidity *
            self.weight.liquidity
        )

    # -------------------------------------------------

    def score_trend(
        self,
        feature,
        score,
    ):
        trend_score = 0
        if feature.trend.above_ma20:
            trend_score += 20
        if feature.trend.breakout20:
            trend_score += 15
        if feature.trend.above_ma60:
            trend_score += 10
        if feature.trend.breakout60:
            trend_score += 10

        score.trend = (
            trend_score *
            self.weight.trend
        )

    # -------------------------------------------------

    def score_momentum(
        self,
        feature,
        score,
    ):
        momentum = 0
        if 50 <= feature.momentum.rsi <= 80:
            momentum += 5
        if feature.momentum.macd_golden:
            momentum += 10
        if feature.momentum.kd_golden:
            momentum += 5

        score.momentum = (
            momentum *
            self.weight.momentum
        )

    # -------------------------------------------------

    def score_institution(
        self,
        feature,
        score,
    ):
        value = (
            feature.institution.foreign_days +
            feature.institution.trust_days
        )
        score.institution = (
            value *
            self.weight.institution
        )

    # -------------------------------------------------

    def score_trade(
        self,
        feature,
        score,
    ):
        trade = 0
        rr = feature.trade.rr
        if rr >= 4:
            trade = 20
        elif rr >= 3:
            trade = 15
        elif rr >= 2:
            trade = 10
        elif rr >= 1.5:
            trade = 5

        score.trade = (
            trade *
            self.weight.trade
        )

    # -------------------------------------------------

    def score_revenue(
        self,
        feature,
        score,
    ):
        revenue = 0
        if feature.revenue.positive_growth:
            revenue += 10

        score.revenue = (
            revenue *
            self.weight.revenue
        )

    # -------------------------------------------------

    def score_theme(
        self,
        feature,
        score,
    ):
        value = 0
        if feature.theme.primary in THEME_SCORE:
            value = THEME_SCORE[
                feature.theme.primary
            ]

        score.theme = (
            value *
            self.weight.theme
        )

    # -------------------------------------------------

    def score_priority(
        self,
        feature,
        score,
    ):
        priority = 0
        score.priority = (
            priority *
            self.weight.priority
        )

    # -------------------------------------------------

    def run(
        self,
        feature,
    ):
        score = ScoreResult()

        self.score_market(feature, score)
        self.score_trend(feature, score)
        self.score_momentum(feature, score)
        self.score_institution(feature, score)
        self.score_trade(feature, score)
        self.score_revenue(feature, score)
        self.score_theme(feature, score)
        self.score_priority(feature, score)

        score.total = (
            score.money +
            score.liquidity +
            score.trend +
            score.momentum +
            score.institution +
            score.trade +
            score.revenue +
            score.theme +
            score.priority
        )

        # -------------------------------------------------
        # Enterprise Output（必須縮排在 run 方法內部）
        # -------------------------------------------------

        # AI 品質
        if score.total >= 90:
            score.quality = "★★★★★"
        elif score.total >= 80:
            score.quality = "★★★★☆"
        elif score.total >= 70:
            score.quality = "★★★☆☆"
        elif score.total >= 60:
            score.quality = "★★☆☆☆"
        else:
            score.quality = "★☆☆☆☆"

        # AI 建議
        if score.total >= 90:
            score.action = "強力買進"
        elif score.total >= 80:
            score.action = "買進"
        elif score.total >= 70:
            score.action = "觀察"
        else:
            score.action = "略過"

        # AI 風險
        rr = feature.trade.rr

        if rr >= 4:
            score.risk = "低"
        elif rr >= 3:
            score.risk = "中低"
        elif rr >= 2:
            score.risk = "中"
        else:
            score.risk = "高"

        # 建議持股天數
        if score.total >= 90:
            score.holding_days = "20~30 天"
        elif score.total >= 80:
            score.holding_days = "10~20 天"
        elif score.total >= 70:
            score.holding_days = "5~10 天"
        else:
            score.holding_days = "1~5 天"

        # AI 評論
        score.comment = (
            f"AI 評分 {score.total:.1f} 分，"
            f"RR={rr}，"
            f"建議：{score.action}"
        )

        # 進場時機
        if feature.trend.above_ma20 and feature.momentum.macd_golden:
            score.entry_timing = "立即"
        elif feature.trend.above_ma20:
            score.entry_timing = "等待拉回"
        else:
            score.entry_timing = "觀察"

        return score