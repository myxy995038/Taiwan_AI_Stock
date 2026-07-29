"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

AI Weight Manager
==========================================================
"""

from dataclasses import dataclass, asdict
     
    
@dataclass
class AIWeight:

    # =====================================
    # Feature Weight（Learning Center）
    # =====================================

    ma20: float = 1.0

    new_high: float = 1.0

    macd: float = 1.0

    kd: float = 1.0

    rsi: float = 1.0

    # =====================================
    # Score Weight（Engine）
    # =====================================

    money: float = 1.0

    liquidity: float = 1.0

    trend: float = 1.0

    momentum: float = 1.0

    institution: float = 1.0

    trade: float = 1.0

    revenue: float = 1.0

    theme: float = 1.0

    priority: float = 1.0
    
    

    def to_dict(self):

        return asdict(self)

    def reset(self):

        for key in self.__dict__:

            setattr(self, key, 1.0)