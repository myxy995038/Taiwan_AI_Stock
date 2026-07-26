from AI_ENGINE.learning import (
    LearningRecord,
    StatisticsEngine,
)

records = [

    LearningRecord(
        stock_id="2330",
        success=True,
        return_rate=4.5,
        theme="AI",
    ),

    LearningRecord(
        stock_id="2317",
        success=False,
        return_rate=-2.0,
        theme="AI",
    ),

    LearningRecord(
        stock_id="2454",
        success=True,
        return_rate=8.2,
        theme="半導體",
    ),

]

engine = StatisticsEngine(records)

print("=" * 60)

print("Summary")
print(engine.summary())

print()

print("Theme Statistics")
print(engine.theme_statistics())

print("=" * 60)