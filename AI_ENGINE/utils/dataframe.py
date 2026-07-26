"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

dataframe.py

DataFrame Utilities
==========================================================
"""

import pandas as pd


# ----------------------------------------------------------
# Empty
# ----------------------------------------------------------

def is_empty(df):

    return df is None or df.empty


# ----------------------------------------------------------
# Last Row
# ----------------------------------------------------------

def last_row(df):

    if is_empty(df):

        return None

    return df.iloc[-1]


# ----------------------------------------------------------
# First Row
# ----------------------------------------------------------

def first_row(df):

    if is_empty(df):

        return None

    return df.iloc[0]


# ----------------------------------------------------------
# Has Column
# ----------------------------------------------------------

def has_column(df, column):

    return column in df.columns


# ----------------------------------------------------------
# Safe Sort
# ----------------------------------------------------------

def safe_sort(df, by, ascending=False):

    if is_empty(df):

        return df

    if by not in df.columns:

        return df

    return df.sort_values(
        by=by,
        ascending=ascending,
    )


# ----------------------------------------------------------
# Reset Index
# ----------------------------------------------------------

def reset(df):

    return df.reset_index(drop=True)


# ----------------------------------------------------------
# Remove Duplicate
# ----------------------------------------------------------

def remove_duplicate(df):

    return df.drop_duplicates().reset_index(drop=True)


# ----------------------------------------------------------
# To Numeric
# ----------------------------------------------------------

def to_numeric(df, columns):

    for col in columns:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce",
            )

    return df