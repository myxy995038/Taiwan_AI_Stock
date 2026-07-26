from AI_ENGINE.engine import ScoringEngine

from AI_ENGINE.score import AIWeight

from AI_ENGINE.feature.models import (
    FeatureResult,
    MarketFeatureResult,
    TrendFeatureResult,
    MomentumFeatureResult,
    InstitutionFeatureResult,
    TradeFeatureResult,
    ThemeFeatureResult,
    RevenueFeatureResult,
)

feature = FeatureResult()

feature.market = MarketFeatureResult(
    money=30,
    liquidity=20,
)

feature.trend = TrendFeatureResult(
    above_ma20=True,
    breakout20=True,
)

feature.momentum = MomentumFeatureResult(
    rsi=65,
    macd_golden=True,
    kd_golden=True,
)

feature.institution = InstitutionFeatureResult(
    foreign_days=5,
    trust_days=2,
)

feature.trade = TradeFeatureResult(
    rr=3,
)

feature.theme = ThemeFeatureResult(
    names=["AI", "CPO"],
)

feature.revenue = RevenueFeatureResult(
    positive_growth=True,
)

engine = ScoringEngine(AIWeight())

score = engine.run(feature)

print("=" * 60)
print(score)
print()
print("TOTAL =", score.total)
print("=" * 60)