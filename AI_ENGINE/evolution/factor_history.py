import pandas as pd
from pathlib import Path

from AI_ENGINE.utils.schema import SchemaManager
from AI_ENGINE.utils.schemas import FACTOR_HISTORY_SCHEMA


class FactorHistory:

    def __init__(self, file_path):

        self.file = Path(file_path)

    def load(self):

        if not self.file.exists():

            return pd.DataFrame()

        df = pd.read_excel(self.file)

        df = SchemaManager.ensure(
            df,
            FACTOR_HISTORY_SCHEMA,
        )

        return df

    def save(self, df):

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_excel(
            self.file,
            index=False,
        )