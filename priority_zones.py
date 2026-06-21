import pandas as pd

df = pd.read_csv("data/parking.csv")

priority = (
    df.groupby("location")
    .size()
    .reset_index(name="violations")
)

priority = priority.sort_values(
    by="violations",
    ascending=False
)

def risk_level(x):
    if x >= 3500:
        return "High"
    elif x >= 2500:
        return "Medium"
    else:
        return "Low"

priority["risk"] = priority["violations"].apply(risk_level)

print(priority.head(20))