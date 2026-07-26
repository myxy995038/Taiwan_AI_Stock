"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Trend Feature
==========================================================
"""

from AI_ENGINE.feature.models import TrendFeatureResult


class TrendFeature:

    """
    趨勢特徵

    只負責產生 Feature
    不做任何評分
    """

    def run(self, latest, df):

        feature = TrendFeatureResult()

        # ---------- MA20 ----------
        feature.ma20 = float(latest["MA20"])

        # ---------- MA60 ----------
        feature.ma60 = float(latest["MA60"])

        # ---------- 是否站上 MA20 ----------
        feature.above_ma20 = bool(
            latest["close"] > latest["MA20"]
        )

        # ---------- 是否站上 MA60 ----------
        feature.above_ma60 = bool (
            latest["close"] > latest["MA60"]
        )

        # ---------- 是否創20日新高 ----------
        feature.breakout20 = bool (
            latest["close"]
            >= df["close"].tail(20).max()
        )

        # ---------- 是否創60日新高 ----------
        feature.breakout60 = bool (
            latest["close"]
            >= df["close"].tail(60).max()
        )

        return feature