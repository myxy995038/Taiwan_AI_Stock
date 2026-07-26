from AI_ENGINE.engine.money import MoneyScoreEngine

engine = MoneyScoreEngine()

print("=" * 60)

for money in [

    50000000000,

    20000000000,

    10000000000,

    5000000000,

    None

]:

    print(

        money,

        "->",

        engine.calculate(money)

    )

print("=" * 60)