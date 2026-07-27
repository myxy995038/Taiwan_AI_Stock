from AI_ENGINE.pipeline import ScoringPipeline

pipeline = ScoringPipeline()

result = pipeline.run(

    money_score=30,
    liquidity_score=20,
    trend_score=35,
    momentum_score=20,
    institution_score=7,
    trade_score=15,
    revenue_score=10,
    theme_score=30,
    priority_score=0,

)

print(result)

print()

print("TOTAL =", result.total)