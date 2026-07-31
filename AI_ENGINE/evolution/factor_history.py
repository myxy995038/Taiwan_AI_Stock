import pandas as pd
from pathlib import Path


class FactorHistory:

    def __init__(self, file_path):

        self.file = Path(file_path)

    def load(self):

        if not self.file.exists():
            return pd.DataFrame()

        return pd.read_excel(self.file)

    def save(self, df):

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_excel(
            self.file,
            index=False,
        )