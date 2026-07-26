from AI_ENGINE.feature import RevenueFeature

engine = RevenueFeature()

result = engine.run(

    monthly_revenue=325000000,

    revenue_growth=12.5,

)

print("=" * 60)

print(result)

print()

print(result.monthly_revenue)

print(result.revenue_growth)

print(result.positive_growth)

print("=" * 60)