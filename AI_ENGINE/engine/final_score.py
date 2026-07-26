"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Final Score
==========================================================
"""

from dataclasses import dataclass


@dataclass
class ScoreResult:
    money: float = 0
    liquidity: float = 0
    trend: float = 0
    momentum: float = 0
    institution: float = 0
    revenue: float = 0
    limitup: float = 0
    rr: float = 0
    theme: float = 0

    @property
    def total(self):

        return (
            self.money
            + self.liquidity
            + self.trend
            + self.momentum
            + self.institution
            + self.revenue
            + self.limitup
            + self.rr
            + self.theme
        )