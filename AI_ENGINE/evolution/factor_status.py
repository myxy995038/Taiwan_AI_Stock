import pandas as pd
from pathlib import Path


class FactorStatus:

    def __init__(self, history_folder="history"):

        self.file = Path(history_folder) / "FACTOR_STATUS.xlsx"

    # ------------------------------------------------

    def load(self):

        if self.file.exists():

            return pd.read_excel(self.file)

        return pd.DataFrame(columns=[

            "Factor",

            "Enabled",

            "DisableCount",

            "ResurrectionCount",

            "LastStatus",

        ])

    # ------------------------------------------------

    def save(self, df):

        df.to_excel(

            self.file,

            index=False,

        )