from AI_ENGINE.learning import (
    LearningRecord,
    StatisticsEngine,
)

records = [

    LearningRecord(
        stock_id="2330",
        success=True,
        return_rate=4.5,
        money_score=30,
        trend_score=35,
        momentum_score=20,
        institution_score=8,
        trade_score=15,
        revenue_score=10,
        theme_score=30,
        theme="AI",
    ),

    LearningRecord(
        stock_id="2317",
        success=False,
        return_rate=-2.0,
        money_score=10,
        trend_score=15,
        momentum_score=5,
        institution_score=2,
        trade_score=5,
        revenue_score=0,
        theme_score=20,
        theme="AI",
    ),

]

engine = StatisticsEngine(records)

print("=" * 60)

df = engine.factor_statistics()

print(df)

print("=" * 60)