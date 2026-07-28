"""
==========================================================
Taiwan AI Stock System
Scoring Pipeline
==========================================================
"""

from AI_ENGINE.engine.scoring_engine import ScoringEngine


class ScoringPipeline:

    def __init__(self):
        self.engine = ScoringEngine()

    def run(self, feature):
        """
        接收 FeatureResult
        回傳 ScoreResult
        """
        return self.engine.run(feature)