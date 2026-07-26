import pandas as pd

from AI_ENGINE.feature import MomentumFeature

latest = pd.Series({

    "RSI": 65,

    "MACD": 2.3,

    "MACD_SIGNAL": 1.8,

    "K": 82,

    "D": 70,

})

engine = MomentumFeature()

result = engine.run(latest)

print("=" * 60)

print(result)

print()

print(result.rsi)

print(result.macd)

print(result.macd_signal)

print(result.macd_golden)

print(result.k)

print(result.d)

print(result.kd_golden)

print("=" * 60)