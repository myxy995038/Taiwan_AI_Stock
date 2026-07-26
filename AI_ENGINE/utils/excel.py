"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

excel.py

Excel Utilities
==========================================================
"""

from pathlib import Path

import pandas as pd

from AI_ENGINE.config import PATHS
from AI_ENGINE.logger import logger


# ----------------------------------------------------------
# Save DataFrame
# ----------------------------------------------------------

def save_excel(df, filename, folder=None, index=False):
    """
    儲存 DataFrame 成 Excel

    Parameters
    ----------
    df : pandas.DataFrame
    filename : str
    folder : Path or str
    index : bool
    """

    if folder is None:
        folder = PATHS.REPORT_DIR

    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)

    filepath = folder / filename

    df.to_excel(filepath, index=index)

    logger.info(f"Excel Saved : {filepath}")

    return filepath


# ----------------------------------------------------------
# Read Excel
# ----------------------------------------------------------

def read_excel(filepath):
    """
    讀取 Excel
    """

    filepath = Path(filepath)

    return pd.read_excel(filepath)


# ----------------------------------------------------------
# Sheet Names
# ----------------------------------------------------------

def list_sheet(filepath):

    filepath = Path(filepath)

    excel = pd.ExcelFile(filepath)

    return excel.sheet_names