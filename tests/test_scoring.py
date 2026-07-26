from AI_ENGINE.engine.scoring_engine import ScoringEngine
from AI_ENGINE.feature.models import (
    FeatureResult,
    MarketFeatureResult,
    TrendFeatureResult,
    MomentumFeatureResult,
    InstitutionFeatureResult,
    TradeFeatureResult,
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
    rr=3.5,
)

from AI_ENGINE.score import AIWeight

weight = AIWeight()

weight.money = 1.5

weight.trade = 2.0

engine = ScoringEngine(weight)

score = engine.run(feature)

print("=" * 60)
print(score)
print()
print("Total =", score.total)
print("=" * 60)