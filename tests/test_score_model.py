from AI_ENGINE.score import ScoreResult

score = ScoreResult()

score.money = 30

score.trend = 20

score.trade = 15

score.total = (

    score.money +

    score.trend +

    score.trade

)

print("=" * 60)

print(score)

print()

print(score.total)

print("=" * 60)