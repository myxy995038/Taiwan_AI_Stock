import pandas as pd
from pathlib import Path

from AI_ENGINE.utils.schema import SchemaManager
from AI_ENGINE.utils.schemas import FACTOR_STATUS_SCHEMA


class FactorStatus:

    def __init__(self, history_folder="history"):

        self.file = Path(history_folder) / "FACTOR_STATUS.xlsx"

    # ------------------------------------------------

    def load(self):

        if self.file.exists():

            df = pd.read_excel(self.file)

        else:

            df = pd.DataFrame()

        # 自動補齊所有欄位
        df = SchemaManager.ensure(
            df,
            FACTOR_STATUS_SCHEMA,
        )

        return df

    # ------------------------------------------------

    def save(self, df):

        # 再保險一次，存檔前補欄位
        df = SchemaManager.ensure(
            df,
            FACTOR_STATUS_SCHEMA,
        )

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_excel(
            self.file,
            index=False,
        )