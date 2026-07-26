import pandas as pd

from AI_ENGINE.engine.feature_engine import FeatureEngine

# 建立測試資料
df = pd.DataFrame({
    "close": [100,105,110,115,120,125,130,135,140],
    "MA20": [90,95,100,105,110,115,120,125,130],
    "MA60": [80,85,90,95,100,105,110,115,120],
    "RSI": [45,50,55,60,65,68,70,72,75],
    "MACD": [0.5,0.8,1.0,1.3,1.6,2.0,2.3,2.5,2.8],
    "MACD_SIGNAL": [0.4,0.6,0.8,1.0,1.2,1.5,1.8,2.0,2.2],
    "K": [40,50,60,70,75,80,82,85,88],
    "D": [35,45,55,65,68,72,70,74,80],
})

latest = df.iloc[-1]

engine = FeatureEngine()

feature = engine.run(
    latest=latest,
    df=df,
    trading_money = 65_000_000_000,
    foreign_days=5,
    trust_days=2,
    buy_price=100,
    stop_price=90,
    atr=5,
    themes=["AI", "光通訊", "CPO"],
    monthly_revenue=325_000_000,
    revenue_growth=12.5,
)

print("=" * 60)

print("Market")
print(feature.market)

print("\nTrend")
print(feature.trend)

print("\nMomentum")
print(feature.momentum)

print("\nInstitution")
print(feature.institution)

print("\nTrade")
print(feature.trade)

print("\nTheme")
print(feature.theme)

print("\nRevenue")
print(feature.revenue)

print("=" * 60)