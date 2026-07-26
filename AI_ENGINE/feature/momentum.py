"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Momentum Feature
==========================================================
"""

from AI_ENGINE.feature.models import MomentumFeatureResult


class MomentumFeature:

    """
    動能特徵

    只產生 Feature
    不計分
    """

    def run(self, latest):

        feature = MomentumFeatureResult()

        feature.rsi = float(latest["RSI"])

        feature.macd = float(latest["MACD"])

        feature.macd_signal = float(latest["MACD_SIGNAL"])

        feature.macd_golden = bool(
            latest["MACD"] > latest["MACD_SIGNAL"]
        )

        feature.k = float(latest["K"])

        feature.d = float(latest["D"])

        feature.kd_golden = bool(
            latest["K"] > latest["D"]
        )

        return feature