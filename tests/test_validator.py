import pandas as pd

from AI_ENGINE.utils.validator import *

print("=" * 60)

df = pd.DataFrame({

    "close":[1,2,3],

    "volume":[10,20,30]

})

print(validate_dataframe(df))

print(validate_columns(df, ["close","volume"]))

print(validate_score(90))

print(validate_stock_id("2330"))

print("=" * 60)