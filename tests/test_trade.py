from AI_ENGINE.feature import TradeFeature

engine = TradeFeature()

result = engine.run(

    close_price=120,

    buy_price=100,

    stop_price=90,

    atr=5,

)

print("=" * 60)

print(result)

print()

print(result.buy_price)

print(result.stop_price)

print(result.atr)

print(result.reward)

print(result.risk)

print(result.rr)

print(result.can_trade)

print("=" * 60)