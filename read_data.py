import pandas as pd

df = pd.read_csv("data/parking.csv")

print("First 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)