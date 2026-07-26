import pandas as pd

from AI_ENGINE.feature import TrendFeature

df = pd.DataFrame({

    "close":[
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        123,
        124,
        125,
        126,
        127,
        128,
        129,
        130,
        131,
        132,
        133,
        134,
        135,
        136,
        137,
        138,
        139,
        140,
        141,
        142,
        143,
        144,
        145,
        146,
        147,
        148,
        149,
        150,
        151,
        152,
        153,
        154,
        155,
        156,
        157,
        158,
        159,
    ]
})

df["MA20"] = 140
df["MA60"] = 120

latest = df.iloc[-1]

engine = TrendFeature()

result = engine.run(
    latest,
    df,
)

print("=" * 60)

print(result)

print()

print(result.above_ma20)

print(result.above_ma60)

print(result.breakout20)

print(result.breakout60)

print("=" * 60)