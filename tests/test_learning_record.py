from AI_ENGINE.learning import LearningRecord

record = LearningRecord(

    stock_id="2330",

    stock_name="台積電",

    date="2026-07-25",

    total_score=92,

    money_score=30,

    trend_score=35,

    momentum_score=20,

    institution_score=7,

    trade_score=15,

    revenue_score=10,

    theme_score=30,

    rr=3.8,

    return_rate=4.25,

    holding_days=5,

    success=True,

    theme="AI",

    comment="AI選股成功",

)

print("=" * 60)
print(record)
print()
print(record.stock_id)
print(record.total_score)
print(record.return_rate)
print(record.success)
print(record.theme)
print("=" * 60)