import pandas as pd
import folium

# Load dataset
df = pd.read_csv("data/parking.csv")

# Count violations per location
counts = df["location"].value_counts()

# Calculate average coordinates for each location
hotspots = df.groupby("location").agg({
    "latitude": "mean",
    "longitude": "mean"
})

# Add violation counts
hotspots["violations"] = counts

# Select Top 20 Hotspots
hotspots = hotspots.sort_values(
    by="violations",
    ascending=False
).head(20)

# Create Bengaluru Map
m = folium.Map(
    location=[12.9716, 77.5946],
    zoom_start=11
)

# Add Hotspot Markers
for location, row in hotspots.iterrows():

    violations = row["violations"]

    # Risk Classification
    if violations >= 3500:
        color = "red"
        risk = "High Risk"

    elif violations >= 2500:
        color = "orange"
        risk = "Medium Risk"

    else:
        color = "green"
        risk = "Low Risk"

    # Dynamic Circle Size
    radius = violations / 300

    # Create Marker
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=radius,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.8,

        popup=f"""
        <b>Location:</b><br>{location}<br><br>

        <b>Total Violations:</b> {violations}<br>

        <b>Risk Level:</b> {risk}
        """
    ).add_to(m)

# Save Map
m.save("smart_hotspots.html")

print("✅ Smart Hotspot Map Created Successfully!")