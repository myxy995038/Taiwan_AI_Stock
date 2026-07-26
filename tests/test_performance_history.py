from AI_ENGINE.learning import (
    LearningRecord,
    PerformanceHistory,
)

history = PerformanceHistory(
    "history/performance_history.xlsx"
)

history.clear()

history.add(

    LearningRecord(

        stock_id="2330",

        stock_name="台積電",

        total_score=92,

        return_rate=4.25,

        success=True,

        theme="AI",

    )

)

history.add(

    LearningRecord(

        stock_id="2317",

        stock_name="鴻海",

        total_score=88,

        return_rate=-1.5,

        success=False,

        theme="AI",

    )

)

print("=" * 60)

print("Record Count")

print(history.count())

print()

print(history.to_dataframe())

print()

path = history.save()

print("Saved")

print(path)

print("=" * 60)