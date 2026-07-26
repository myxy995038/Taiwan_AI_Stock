"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Scoring Engine V2
==========================================================
"""

from AI_ENGINE.score import (
    ScoreResult,
    AIWeight,
)

from AI_ENGINE.constants import THEME_SCORE


class ScoringEngine:

    def __init__(self, weight=None):

        if weight is None:
            weight = AIWeight()

        self.weight = weight

    # -----------------------------------------------------
    # Market
    # -----------------------------------------------------

    def score_market(self, feature, score):

        score.money = (
            feature.market.money *
            self.weight.money
        )

        score.liquidity = (
            feature.market.liquidity *
            self.weight.liquidity
        )

    # -----------------------------------------------------
    # Trend
    # -----------------------------------------------------

    def score_trend(self, feature, score):

        trend_score = 0

        if feature.trend.above_ma20:
            trend_score += 20

        if feature.trend.breakout20:
            trend_score += 15

        score.trend = (
            trend_score *
            self.weight.trend
        )

    # -----------------------------------------------------
    # Momentum
    # -----------------------------------------------------

    def score_momentum(self, feature, score):

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

    # -----------------------------------------------------
    # Institution
    # -----------------------------------------------------

    def score_institution(self, feature, score):

        value = (
            feature.institution.foreign_days +
            feature.institution.trust_days
        )

        score.institution = (
            value *
            self.weight.institution
        )

    # -----------------------------------------------------
    # Trade
    # -----------------------------------------------------

    def score_trade(self, feature, score):

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

    # -----------------------------------------------------
    # Revenue
    # -----------------------------------------------------

    def score_revenue(self, feature, score):

        value = 0

        if feature.revenue.positive_growth:
            value = 10

        score.revenue = (
            value *
            self.weight.revenue
        )

    # -----------------------------------------------------
    # Theme
    # -----------------------------------------------------

    def score_theme(self, feature, score):

        value = 0

        for theme in feature.theme.names:
            value += THEME_SCORE.get(theme, 0)

        score.theme = (
            value *
            self.weight.theme
        )

    # -----------------------------------------------------
    # Priority
    # -----------------------------------------------------

    def score_priority(self, feature, score):

        score.priority = 0

    # -----------------------------------------------------
    # Run
    # -----------------------------------------------------

    def run(self, feature):

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

        return score