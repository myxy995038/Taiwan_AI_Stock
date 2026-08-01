"""
==========================================================
History Schemas
==========================================================
"""

PERFORMANCE_SCHEMA = {

    "stock_id": "",
    "stock_name": "",
    "date": "",

    "total_score": 0,

    "money_score": 0,
    "liquidity_score": 0,
    "trend_score": 0,
    "momentum_score": 0,
    "institution_score": 0,
    "trade_score": 0,
    "revenue_score": 0,
    "theme_score": 0,
    "priority_score": 0,

    "rr": 0,

    "return_rate": 0,

    "holding_days": 0,

    "success": False,

    "theme": "",

    "comment": "",

    "quality": "",

    "action": "",

    "entry_timing": ""

}


AI_WEIGHT_SCHEMA = {

    "Factor": "",
    "Weight": 1.0,
    "Enabled": True,

}


FACTOR_HISTORY_SCHEMA = {

    "Factor": "",
    "Samples": 0,
    "Average": 0,
    "SuccessAvg": 0,
    "FailureAvg": 0,
    "FactorPower": 0,
    "SuccessRate": 0,
    "AvgReturn": 0,
    "WeightSuggestion": 1,
    "Enabled": True,

}


FACTOR_STATUS_SCHEMA = {

    "Factor": "",
    "Enabled": True,
    "DisableCount": 0,
    "ResurrectionCount": 0,
    "LastStatus": "Active",

}