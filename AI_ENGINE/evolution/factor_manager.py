from AI_ENGINE.evolution.factor_history import FactorHistory
from AI_ENGINE.evolution.factor_engine import FactorEngine


class FactorManager:

    def __init__(self, history_file):

        self.history = FactorHistory(history_file)

        self.engine = FactorEngine()

    def run(self):

        df = self.history.load()

        return self.engine.evaluate(df)