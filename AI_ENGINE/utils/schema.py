"""
==========================================================
Taiwan AI Stock System
Schema Manager
==========================================================
"""

import pandas as pd


class SchemaManager:

    @staticmethod
    def ensure(df, schema: dict):

        """
        自動補齊 DataFrame 欄位
        """

        if df is None:
            df = pd.DataFrame()

        for col, default in schema.items():

            if col not in df.columns:
                df[col] = default

        return df