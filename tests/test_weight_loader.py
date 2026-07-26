from AI_ENGINE.learning import WeightLoader

loader = WeightLoader(

    "history/AI_WEIGHT.xlsx"

)

weight = loader.load()

print(weight)

print()

print(vars(weight))