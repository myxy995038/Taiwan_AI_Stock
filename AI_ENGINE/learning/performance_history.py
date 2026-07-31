"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Performance History
==========================================================
"""

from dataclasses import asdict
from pathlib import Path
from datetime import datetime

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

    def save(self, backup=True):

        df = self.to_dataframe()

        self.file.parent.mkdir(

            parents=True,

            exist_ok=True,

        )
        
        if backup:

            self.backup()

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
        
    # -------------------------------------------------    
        
        
    def exists(self):

        return self.file.exists()
    
    
    
    # -------------------------------------------------
    
    
    def latest(self):

        if len(self.records) == 0:

            return None

        return self.records[-1]
    
    # -------------------------------------------------
    
    def append(self, record):

        if isinstance(record, LearningRecord):

            self.records.append(record)

        else:

            self.records.append(

                LearningRecord(**record)

            )
    
    
    # -------------------------------------------------
    
    
    
    import shutil
    from datetime import datetime

    def backup(self):

        if not self.exists():

            return

        backup_folder = self.file.parent / "backup"

        backup_folder.mkdir(exist_ok=True)

        backup_file = backup_folder / (

            f"{self.file.stem}_"

            f"{datetime.now():%Y%m%d_%H%M%S}"

            ".xlsx"

        )

        shutil.copy(self.file, backup_file)