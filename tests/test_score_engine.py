from AI_ENGINE.engine import ScoreEngine

engine = ScoreEngine()

result = engine.run(

    trading_money=50000000000

)

print(result)

print(result.total)