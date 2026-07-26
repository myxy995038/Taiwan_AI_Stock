"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Money Score Engine
==========================================================
"""

from AI_ENGINE.logger import logger


class MoneyScoreEngine:
    """
    成交值分數
    """

    def __init__(self):

        self.max_score = 30

    def calculate(self, trading_money):

        if trading_money is None:

            logger.warning("Trading Money is None")

            return 0

        money_yi = trading_money / 100000000

        if money_yi >= 500:
            return 30

        elif money_yi >= 200:
            return 20

        elif money_yi >= 100:
            return 10

        return 0