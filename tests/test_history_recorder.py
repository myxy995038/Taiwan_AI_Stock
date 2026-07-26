from AI_ENGINE.history import HistoryRecorder

from AI_ENGINE.score import ScoreResult

from AI_ENGINE.feature.models import (

    FeatureResult,

    TradeFeatureResult,

    ThemeFeatureResult,

)

score = ScoreResult(

    money=30,

    liquidity=20,

    trend=35,

    momentum=20,

    institution=7,

    trade=15,

    revenue=10,

    theme=30,

    priority=0,

    total=167,

)

feature = FeatureResult()

feature.trade = TradeFeatureResult(

    rr=4.0

)

feature.theme = ThemeFeatureResult(

    primary="AI"

)

recorder = HistoryRecorder(

    "history/performance_history.xlsx"

)

record = recorder.record(

    stock_id="2330",

    stock_name="台積電",

    score=score,

    feature=feature,

    return_rate=5.25,

    holding_days=6,

    success=True,

    comment="Recorder Test",

)

print(record)