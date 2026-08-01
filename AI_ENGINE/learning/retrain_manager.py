"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Retrain Manager
==========================================================
"""

from pathlib import Path

from AI_ENGINE.learning.learning_center import LearningCenter
from AI_ENGINE.evolution.factor_manager import FactorManager


class RetrainManager:

    def __init__(
        self,
        history_folder="history",
    ):

        self.history_folder = Path(history_folder)

        self.performance_file = (
            self.history_folder /
            "performance_history.xlsx"
        )

        self.learning = LearningCenter(
            self.performance_file,
        )

        self.factor = FactorManager(
            self.performance_file,
        )

    # -------------------------------------------------

    def update_history(
        self,
        result_df,
    ):

        print("===================================")
        print("STEP 1 更新 Learning History")
        print("===================================")

        self.learning.append_today(
            result_df,
        )

    # -------------------------------------------------

    def update_factor(self):

        print("===================================")
        print("STEP 2 更新 Factor")
        print("===================================")

        self.factor.run()

    # -------------------------------------------------

    def learning_center(self):

        print("===================================")
        print("STEP 3 AI Learning")
        print("===================================")

        return self.learning.run()

    # -------------------------------------------------

    def run(
        self,
        result_df,
    ):

        self.update_history(
            result_df,
        )

        self.update_factor()

        self.learning_center()

        print("===================================")
        print("AI Retraining Completed")
        print("===================================")