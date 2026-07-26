"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Institution Feature
==========================================================
"""

from AI_ENGINE.feature.models import InstitutionFeatureResult


class InstitutionFeature:

    """
    法人特徵

    只產生 Feature
    不計分
    """

    def run(
        self,
        foreign_days=0,
        trust_days=0,
    ):

        feature = InstitutionFeatureResult()

        feature.foreign_days = int(foreign_days)

        feature.trust_days = int(trust_days)

        feature.foreign_buy = bool(
            foreign_days > 0
        )

        feature.trust_buy = bool(
            trust_days > 0
        )

        return feature