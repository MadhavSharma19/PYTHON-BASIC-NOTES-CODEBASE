# =========================================
# Topic : Time Series Analysis
# =========================================

import pandas as pd

# Creating date range
dates = pd.date_range(

    start="2025-01-01",

    periods=5
)

print(dates)

# Creating DataFrame
df = pd.DataFrame({

    "Date": dates,

    "Sales": [100, 200, 150, 300, 250]
})

print(df)

# Setting date as index
df.set_index("Date", inplace=True)

print(df)

# Monthly data
print(df.resample("D").sum())