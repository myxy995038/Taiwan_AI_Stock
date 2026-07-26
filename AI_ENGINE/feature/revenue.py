"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Revenue Feature
==========================================================
"""

from AI_ENGINE.feature.models import RevenueFeatureResult


class RevenueFeature:

    """
    營收特徵

    只建立 Feature
    不做評分
    """

    def run(
        self,
        monthly_revenue=0,
        revenue_growth=0,
    ):

        feature = RevenueFeatureResult()

        feature.monthly_revenue = float(monthly_revenue)

        feature.revenue_growth = float(revenue_growth)

        feature.positive_growth = (
            revenue_growth > 0
        )

        return feature