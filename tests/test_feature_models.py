from AI_ENGINE.feature import FeatureResult

print("=" * 60)

feature = FeatureResult()

feature.market.money = 30

feature.market.liquidity = 20

feature.risk.rr = 3.5

feature.theme.name = "AI"

print(feature)

print()

print(feature.market.money)

print(feature.market.liquidity)

print(feature.risk.rr)

print(feature.theme.name)

print("=" * 60)