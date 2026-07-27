"""
==========================================================
Taiwan AI Stock System
Scoring Pipeline
==========================================================
"""

from AI_ENGINE.adapter import FeatureAdapter
from AI_ENGINE.learning import WeightLoader
from AI_ENGINE.engine.scoring_engine import ScoringEngine


class ScoringPipeline:

    def __init__(self):

        self.weight_loader = WeightLoader()

        self.engine = ScoringEngine()

    # -------------------------------------------------

    def run(self, **kwargs):

        # 1. Feature Adapter
        
        
        feature = FeatureAdapter.from_colab(
            latest=kwargs["latest"],
            df=kwargs["df"],
            rr=kwargs["rr"],
            rr_score=kwargs["rr_score"],
            theme=kwargs["theme"],
            foreign_days=kwargs["foreign_days"],
            trust_days=kwargs["trust_days"],
)
        
        

        # 2. Load latest AI weight
        weight = self.weight_loader.load()

        # 3. AI Scoring
        result = self.engine.run(
            feature=feature,
            weight=weight,
        )

        return result