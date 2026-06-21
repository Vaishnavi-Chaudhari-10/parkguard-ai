import pandas as pd

df = pd.read_csv("data/parking.csv")

print(df["violation_type"].value_counts().head(10))