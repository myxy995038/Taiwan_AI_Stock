import pandas as pd

from AI_ENGINE.utils.excel import *

df = pd.DataFrame({

    "股票":[
        "2330",
        "2317",
        "2454"
    ],

    "總分":[
        95,
        90,
        88
    ]

})

print("=" * 60)

path = save_excel(df, "test.xlsx")

print(path)

print()

print(read_excel(path))

print()

print(list_sheet(path))

print("=" * 60)