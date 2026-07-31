import pandas as pd
from pathlib import Path


class Dashboard:

    def __init__(self, history_folder="history"):
        self.history = Path(history_folder)

    def load_weight(self):
        file = self.history / "AI_WEIGHT.xlsx"

        if not file.exists():
            return pd.DataFrame()

        return pd.read_excel(file)

    def load_performance(self):
        file = self.history / "performance_history.xlsx"

        if not file.exists():
            return pd.DataFrame()

        return pd.read_excel(file)

    def summary(self):

        weight = self.load_weight()
        perf = self.load_performance()

        if perf.empty:
            return {}

        return {
            "總交易數": len(perf),
            "平均報酬": round(perf["return_rate"].mean(), 2),
            "最高報酬": round(perf["return_rate"].max(), 2),
            "最低報酬": round(perf["return_rate"].min(), 2),
            "勝率": round(perf["success"].mean() * 100, 2),
            "目前權重": weight
        }