import pandas as pd

df = pd.read_csv("data/parking.csv")

print("Total Records:", len(df))
print("Total Violation Types:", df["violation_type"].nunique())
print("Total Vehicle Types:", df["vehicle_type"].nunique())
print("Total Police Stations:", df["police_station"].nunique())