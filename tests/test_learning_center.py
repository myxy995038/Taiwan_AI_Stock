from AI_ENGINE.learning import LearningCenter

center = LearningCenter(

    "history/performance_history.xlsx"

)

weight, factor_df, summary = center.run()

print("=" * 60)

print("Summary")

print(summary)

print()

print("Weight")

print(weight)

print()

print("Factor")

print(factor_df)

print("=" * 60)