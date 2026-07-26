"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Theme Feature
==========================================================
"""

from AI_ENGINE.feature.models import ThemeFeatureResult


class ThemeFeature:

    """
    題材特徵

    不做評分

    只保存題材資訊
    """

    def run(

        self,

        themes,

    ):

        feature = ThemeFeatureResult()

        if isinstance(themes, str):

            themes = [themes]

        feature.names = list(themes)

        if len(feature.names):

            feature.primary = feature.names[0]

        return feature