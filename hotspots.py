import pandas as pd

df = pd.read_csv("data/parking.csv")

top_locations = df["location"].value_counts().head(10)

print(top_locations)