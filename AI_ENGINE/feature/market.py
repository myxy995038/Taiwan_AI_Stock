"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Market Feature
==========================================================
"""

from AI_ENGINE.feature.models import MarketFeatureResult

class MarketFeature:

    def run(self, trading_money=None):

        feature = MarketFeatureResult()

        if trading_money is None:

            return feature

        money_yi = trading_money / 100000000

        if money_yi >= 500:

            feature.money = 30

        elif money_yi >= 200:

            feature.money = 20

        elif money_yi >= 100:

            feature.money = 10

        else:

            feature.money = 0

        #
        # liquidity
        # 下一步加入
        #

        return feature