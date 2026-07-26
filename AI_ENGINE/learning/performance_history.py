"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Performance History
==========================================================
"""

from dataclasses import asdict
from pathlib import Path

import pandas as pd

from AI_ENGINE.learning.models import LearningRecord


class PerformanceHistory:

    def __init__(self, file_path):

        self.file = Path(file_path)

        self.records = []

    # -------------------------------------------------

    def add(self, record: LearningRecord):

        self.records.append(record)

    # -------------------------------------------------

    def clear(self):

        self.records = []

    # -------------------------------------------------

    def count(self):

        return len(self.records)

    # -------------------------------------------------

    def to_dataframe(self):

        return pd.DataFrame(

            [asdict(r) for r in self.records]

        )

    # -------------------------------------------------

    def save(self):

        df = self.to_dataframe()

        self.file.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        df.to_excel(

            self.file,

            index=False,

        )

        return self.file

    # -------------------------------------------------

    def load(self):

        if not self.file.exists():

            self.records = []

            return []

        df = pd.read_excel(self.file)

        self.records = [

            LearningRecord(**row)

            for row in df.to_dict(

                orient="records"

            )

        ]

        return self.records