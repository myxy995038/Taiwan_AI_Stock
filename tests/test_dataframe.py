import pandas as pd

from AI_ENGINE.utils.dataframe import *

df = pd.DataFrame({

    "A":[1,2,3],

    "B":[4,5,6]

})

print("="*60)

print(is_empty(df))

print()

print(first_row(df))

print()

print(last_row(df))

print()

print(has_column(df,"A"))

print(has_column(df,"C"))

print()

print(safe_sort(df,"B"))

print()

print(remove_duplicate(df))

print("="*60)