import pandas as pd
import folium
from folium.plugins import HeatMap

# Load dataset
df = pd.read_csv("data/parking.csv")

# Remove rows with missing coordinates
df = df.dropna(subset=["latitude", "longitude"])

# Create Bengaluru map
m = folium.Map(
    location=[12.9716, 77.5946],
    zoom_start=11
)

# Heatmap data
heat_data = df[["latitude", "longitude"]].values.tolist()

# Add heatmap
HeatMap(heat_data).add_to(m)

# Save map
m.save("parking_heatmap.html")

print("Heatmap Created Successfully!")