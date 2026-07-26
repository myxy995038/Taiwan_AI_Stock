"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Trade Feature
==========================================================
"""

from AI_ENGINE.feature.models import TradeFeatureResult


class TradeFeature:

    """
    交易特徵

    只產生 Feature
    不做任何評分
    """

    def run(
        self,
        close_price,
        buy_price,
        stop_price,
        atr,
    ):

        feature = TradeFeatureResult()

        feature.buy_price = float(buy_price)

        feature.stop_price = float(stop_price)

        feature.atr = float(atr)

        feature.reward = (
            close_price - buy_price
        )

        feature.risk = (
            buy_price - stop_price
        )

        if feature.risk > 0:

            feature.rr = round(

                feature.reward /
                feature.risk,

                2

            )

        else:

            feature.rr = 0

        feature.can_trade = (

            feature.rr >= 2

        )

        return feature