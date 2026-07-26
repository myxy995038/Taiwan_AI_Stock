from AI_ENGINE.feature import InstitutionFeature

engine = InstitutionFeature()

result = engine.run(
    foreign_days=5,
    trust_days=2,
)

print("=" * 60)

print(result)

print()

print(result.foreign_days)

print(result.trust_days)

print(result.foreign_buy)

print(result.trust_buy)

print("=" * 60)