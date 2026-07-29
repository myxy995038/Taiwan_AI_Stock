"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Weight Loader
==========================================================
"""

from pathlib import Path
import pandas as pd

from AI_ENGINE.score import AIWeight


class WeightLoader:

    def __init__(

        self,

        file_path="history/AI_WEIGHT.xlsx",

    ):

        self.file = Path(file_path)

    # -------------------------------------------------

    def load(self):

        #
        # 如果沒有 AI_WEIGHT
        # 使用預設權重
        #

        if not self.file.exists():

            return AIWeight()

        df = pd.read_excel(self.file)

        data = {}

        for _, row in df.iterrows():

            key = row["Factor"]

            value = row["Weight"]

            data[key] = value

            
            
            
        return AIWeight(

            # ==========================
            # Feature Weight
            # ==========================

            ma20=data.get("ma20", 1.0),

            new_high=data.get("new_high", 1.0),

            macd=data.get("macd", 1.0),

            kd=data.get("kd", 1.0),

            rsi=data.get("rsi", 1.0),

            # ==========================
            # Score Weight
            # ==========================

            money=data.get("money", 1.0),

            liquidity=data.get("liquidity", 1.0),

            trend=data.get("trend", 1.0),

            momentum=data.get("momentum", 1.0),

            institution=data.get("institution", 1.0),

            trade=data.get("trade", 1.0),

            revenue=data.get("revenue", 1.0),

            theme=data.get("theme", 1.0),

            priority=data.get("priority", 1.0),

        )
            

      