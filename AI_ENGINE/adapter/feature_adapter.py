"""
Feature Adapter V2

Colab
↓

FeatureResult

只保存 Feature
不保存 Score
"""

from AI_ENGINE.feature import FeatureResult


class FeatureAdapter:

    @staticmethod
    def from_colab(
        *,
        latest,
        df,
        rr,
    ):

        feature = FeatureResult()

        # =====================================================
        # Market
        # =====================================================

        feature.market.money = float(latest["Trading_money"])

        feature.market.liquidity = float(latest["MA20_VOLUME"])

        # =====================================================
        # Trend
        # =====================================================

        feature.trend.ma20 = float(latest["MA20"])

        feature.trend.ma60 = float(latest["MA60"])

        feature.trend.above_ma20 = (
            latest["close"] > latest["MA20"]
        )

        feature.trend.above_ma60 = (
            latest["close"] > latest["MA60"]
        )

        feature.trend.breakout20 = (
            latest["close"] >=
            df["close"].tail(20).max()
        )

        feature.trend.breakout60 = (
            latest["close"] >=
            df["close"].tail(60).max()
        )

        # =====================================================
        # Momentum
        # =====================================================

        feature.momentum.rsi = float(
            latest["RSI"]
        )

        feature.momentum.macd = float(
            latest["MACD"]
        )

        feature.momentum.macd_signal = float(
            latest["MACD_SIGNAL"]
        )

        feature.momentum.macd_golden = (
            latest["MACD"] >
            latest["MACD_SIGNAL"]
        )

        feature.momentum.k = float(
            latest["K"]
        )

        feature.momentum.d = float(
            latest["D"]
        )

        feature.momentum.kd_golden = (
            latest["K"] >
            latest["D"]
        )

        # =====================================================
        # Trade
        # =====================================================

        feature.trade.rr = rr

        return feature