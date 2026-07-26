from AI_ENGINE.score import AIWeight

weight = AIWeight()

print("=" * 60)

print(weight)

print()

weight.money = 1.25

weight.trade = 0.80

print(weight.to_dict())

print()

weight.reset()

print(weight)

print("=" * 60)