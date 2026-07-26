from AI_ENGINE.learning import (
    LearningRecord,
    StatisticsEngine,
    WeightLearner,
)

records = [

    LearningRecord(

        stock_id="2330",

        success=True,

        money_score=30,

        trend_score=35,

        momentum_score=20,

        institution_score=8,

        trade_score=20,

        revenue_score=10,

        theme_score=30,

        return_rate=4.5,

    ),

    LearningRecord(

        stock_id="2317",

        success=False,

        money_score=10,

        trend_score=15,

        momentum_score=5,

        institution_score=2,

        trade_score=5,

        revenue_score=0,

        theme_score=20,

        return_rate=-2,

    ),

]

statistics = StatisticsEngine(records)

factor_df = statistics.factor_statistics()

learner = WeightLearner()

weight = learner.learn(

    factor_df,

)

print("=" * 60)

print(weight)

print()

print(weight.to_dict())

print("=" * 60)