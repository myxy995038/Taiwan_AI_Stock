"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

validator.py

Validation Utilities
==========================================================
"""

import pandas as pd


# ----------------------------------------------------------
# DataFrame
# ----------------------------------------------------------

def validate_dataframe(df):

    if df is None:
        raise ValueError("DataFrame is None")

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input is not DataFrame")

    if df.empty:
        raise ValueError("DataFrame is Empty")

    return True


# ----------------------------------------------------------
# Columns
# ----------------------------------------------------------

def validate_columns(df, columns):

    validate_dataframe(df)

    missing = []

    for col in columns:

        if col not in df.columns:

            missing.append(col)

    if missing:

        raise KeyError(f"Missing Columns : {missing}")

    return True


# ----------------------------------------------------------
# Score
# ----------------------------------------------------------

def validate_score(score):

    if score is None:

        raise ValueError("Score is None")

    if score < 0:

        raise ValueError("Score < 0")

    if score > 100:

        raise ValueError("Score > 100")

    return True


# ----------------------------------------------------------
# Stock ID
# ----------------------------------------------------------

def validate_stock_id(stock_id):

    stock_id = str(stock_id)

    if len(stock_id) != 4:

        raise ValueError("Stock ID Length Error")

    if not stock_id.isdigit():

        raise ValueError("Stock ID Format Error")

    return True


# ----------------------------------------------------------
# File Exists
# ----------------------------------------------------------

def validate_file(path):

    from pathlib import Path

    path = Path(path)

    if not path.exists():

        raise FileNotFoundError(path)

    return True