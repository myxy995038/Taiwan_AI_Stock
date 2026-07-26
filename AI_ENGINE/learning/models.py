"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Learning Models
==========================================================
"""

from dataclasses import dataclass


@dataclass
class LearningRecord:
    """
    AI 每一筆學習資料
    """

    stock_id: str = ""

    stock_name: str = ""

    date: str = ""

    total_score: float = 0

    money_score: float = 0

    liquidity_score: float = 0

    trend_score: float = 0

    momentum_score: float = 0

    institution_score: float = 0

    trade_score: float = 0

    revenue_score: float = 0

    theme_score: float = 0

    priority_score: float = 0

    rr: float = 0

    return_rate: float = 0

    holding_days: int = 0

    success: bool = False

    theme: str = ""

    comment: str = ""