"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Score Data Models
==========================================================
"""

from dataclasses import dataclass
  
    
@dataclass
class ScoreResult:

    # ---------- Feature Score ----------

    money: float = 0
    liquidity: float = 0
    trend: float = 0
    momentum: float = 0
    institution: float = 0
    trade: float = 0
    revenue: float = 0
    theme: float = 0
    priority: float = 0

    # ---------- Total ----------

    total: float = 0

    # ---------- Enterprise Output ----------

    quality: str = ""

    action: str = ""

    risk: str = ""

    holding_days: str = ""

    entry_timing: str = ""

    comment: str = ""