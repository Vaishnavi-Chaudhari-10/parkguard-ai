import pandas as pd

df = pd.read_csv("data/parking.csv")

print(df["created_datetime"].head(10))