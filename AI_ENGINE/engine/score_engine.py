from AI_ENGINE.engine.final_score import ScoreResult
from AI_ENGINE.engine.money import MoneyScoreEngine


class ScoreEngine:

    def __init__(self):

        self.result = ScoreResult()

        self.money_engine = MoneyScoreEngine()

    def run(self, trading_money=None):

        self.result.money = self.money_engine.calculate(
            trading_money
        )

        return self.result