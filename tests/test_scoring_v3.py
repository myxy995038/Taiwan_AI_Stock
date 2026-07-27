from AI_ENGINE.engine import ScoringEngine
from AI_ENGINE.engine.feature_engine import FeatureEngine

feature = FeatureEngine().run(
    trading_money=60000000000,
)

score = ScoringEngine().run(feature)

print(score)
print()
print("TOTAL =", score.total)