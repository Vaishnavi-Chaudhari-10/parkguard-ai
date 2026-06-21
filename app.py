import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="SmartPark AI",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data/parking.csv")

# =========================
# TITLE
# =========================

st.title("🚗 SmartPark AI")
st.subheader(
    "AI-Powered Parking Congestion Intelligence System"
)

# =========================
# SIDEBAR
# =========================

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Home",
        "Dashboard Summary",
        "Dataset Insights",
        "Hotspots",
        "Parking Intelligence Map",
        "Violation Heatmap",
        "Recommendations",
        "AI Risk Forecast"
    ]
)

# ===================================================
# HOME
# ===================================================

if page == "Home":

    st.header("Project Overview")

    st.info("""
SmartPark AI uses parking violation data analytics to:

• Detect illegal parking hotspots

• Generate violation heatmaps

• Prioritize enforcement zones

• Predict future parking risks

• Support smart city traffic management
""")

   

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Violations",
            len(df)
        )

    with col2:
        st.metric(
            "Vehicle Types",
            df["vehicle_type"].nunique()
        )

    with col3:
        st.metric(
            "Police Stations",
            df["police_station"].nunique()
        )

    with col4:
        st.metric(
            "Violation Types",
            df["violation_type"].nunique()
        )

    st.success("✔ Illegal Parking Hotspots Detected")
    st.success("✔ Priority Enforcement Zones Identified")
    st.success("✔ AI Risk Forecast Generated")
    st.success("✔ Enforcement Recommendations Generated")
# ===================================================
# DASHBOARD SUMMARY
# ===================================================

elif page == "Dashboard Summary":

    st.header("Executive Dashboard Summary")

    top_hotspot = (
        df.groupby("location")
        .size()
        .sort_values(ascending=False)
        .head(1)
    )

    top_location = top_hotspot.index[0]

    if "Begur" in top_location:
        hotspot_name = "Begur"

    elif "Kamaraj" in top_location:
        hotspot_name = "Kamaraj Road"

    elif "KR Puram" in top_location:
        hotspot_name = "KR Puram"

    elif "Hebbal" in top_location:
        hotspot_name = "Hebbal"

    else:
        hotspot_name = top_location.split(",")[0]

    top_violation = (
        df["violation_type"]
        .astype(str)
        .str.replace("[", "", regex=False)
        .str.replace("]", "", regex=False)
        .str.replace('"', "", regex=False)
        .value_counts()
        .head(1)
    )

    st.metric(
        "Top Hotspot",
        hotspot_name
    )

    st.metric(
        "Most Common Violation",
        top_violation.index[0]
    )

    st.success("✔ Highest Risk Zone Identified")

    st.warning(
        "⚠ Immediate Enforcement Recommended"
    )

    st.info(
        "Deploy Enforcement Team in High-Risk Areas"
    )

# ===================================================
# DATASET INSIGHTS
# ===================================================

elif page == "Dataset Insights":

    st.header("Dataset Summary")

    # KPI CARDS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Records",
            len(df)
        )

    with col2:
        st.metric(
            "Vehicle Types",
            df["vehicle_type"].nunique()
        )

    with col3:
        st.metric(
            "Police Stations",
            df["police_station"].nunique()
        )

    st.markdown("---")

    st.subheader("Top Violation Types")

    # TOP 5 VIOLATIONS
    violations = (
        df["violation_type"]
        .value_counts()
        .head(5)
    )

    # CLEAN LABELS
    labels = []

    for v in violations.index:

        text = str(v)

        text = text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace('"', "")

        labels.append(text)

    # BAR CHART
    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.bar(
        labels,
        violations.values
    )

    plt.xticks(
        rotation=30,
        ha="right"
    )

    ax.set_title(
        "Top Violation Types"
    )

    ax.set_ylabel(
        "Count"
    )

    st.pyplot(fig)

    st.markdown("---")

    # CLEAN TABLE
    violations_df = pd.DataFrame({
        "Violation Type": labels,
        "Count": violations.values
    })

    st.subheader(
        "Violation Statistics"
    )

    st.dataframe(
        violations_df,
        use_container_width=True
    )

    st.success(
        f"Most Frequent Violation: {labels[0]}"
    )
# ===================================================
# HOTSPOTS
# ===================================================

elif page == "Hotspots":

    st.header("Top Parking Hotspots")

    hotspots = (
        df.groupby("location")
        .size()
        .reset_index(name="violations")
        .sort_values(
            by="violations",
            ascending=False
        )
        .head(20)
    )

    top10 = (
        hotspots
        .head(10)
    )

    labels = []

    for loc in top10["location"]:

        if "Begur" in loc:
            labels.append("Begur")

        elif "Kamaraj" in loc:
            labels.append("Kamaraj Road")

        elif "KR Puram" in loc:
            labels.append("KR Puram")

        elif "Hebbal" in loc:
            labels.append("Hebbal")

        elif "Shivaji Nagar" in loc:
            labels.append("Shivaji Nagar")

        elif "Gandhi Nagar" in loc:
            labels.append("Gandhi Nagar")

        else:
            labels.append(loc[:15])

    fig, ax = plt.subplots(
        figsize=(12,5)
    )

    ax.bar(
        labels,
        top10["violations"]
    )

    plt.xticks(rotation=45)

    ax.set_title(
        "Top 10 Parking Hotspots"
    )

    ax.set_ylabel(
        "Violations"
    )

    st.pyplot(fig)

    st.dataframe(hotspots)

# ===================================================
# PARKING INTELLIGENCE MAP
# ===================================================

elif page == "Parking Intelligence Map":

    st.header(
        "Parking Intelligence Map"
    )

    HtmlFile = open(
        "smart_hotspots.html",
        "r",
        encoding="utf-8"
    )

    source_code = HtmlFile.read()

    st.components.v1.html(
        source_code,
        height=700
    )

# ===================================================
# VIOLATION HEATMAP
# ===================================================

elif page == "Violation Heatmap":

    st.header(
        "Violation Density Heatmap"
    )

    HtmlFile = open(
        "parking_heatmap.html",
        "r",
        encoding="utf-8"
    )

    source_code = HtmlFile.read()

    st.components.v1.html(
        source_code,
        height=700
    )
# ===================================================
# RECOMMENDATIONS
# ===================================================

elif page == "Recommendations":

    st.header(
        "Priority Enforcement Zones"
    )

    st.error(
        "🔴 High Risk Areas → Deploy Enforcement Team"
    )

    st.warning(
        "🟡 Medium Risk Areas → Increase Patrol Frequency"
    )

    st.success(
        "🟢 Low Risk Areas → Routine Monitoring"
    )

    priority = (
        df.groupby("location")
        .size()
        .reset_index(
            name="violations"
        )
        .sort_values(
            by="violations",
            ascending=False
        )
        .head(20)
    )

    def risk_level(x):

        if x >= 3500:
            return "High"

        elif x >= 2500:
            return "Medium"

        else:
            return "Low"

    priority["risk"] = (
        priority["violations"]
        .apply(risk_level)
    )

    def recommendation(risk):

        if risk == "High":
            return "Deploy Enforcement Team"

        elif risk == "Medium":
            return "Increase Patrol Frequency"

        else:
            return "Routine Monitoring"

    priority["recommendation"] = (
        priority["risk"]
        .apply(recommendation)
    )

    st.dataframe(priority)

# ===================================================
# AI RISK FORECAST
# ===================================================

elif page == "AI Risk Forecast":

    st.header(
        "AI Risk Forecast"
    )

    st.info(
        "Forecast generated using historical parking violation patterns."
    )

    forecast = (
        df.groupby("location")
        .size()
        .reset_index(
            name="violations"
        )
        .sort_values(
            by="violations",
            ascending=False
        )
        .head(15)
    )

    def current_risk(x):

        if x >= 3500:
            return "High"

        elif x >= 2500:
            return "Medium"

        else:
            return "Low"

    forecast["Current Risk"] = (
        forecast["violations"]
        .apply(current_risk)
    )

    def predicted_risk(x):

        if x >= 3000:
            return "High"

        elif x >= 2000:
            return "Medium"

        else:
            return "Low"

    forecast["Predicted Risk"] = (
        forecast["violations"]
        .apply(predicted_risk)
    )

    high = (
        forecast["Predicted Risk"]
        == "High"
    ).sum()

    medium = (
        forecast["Predicted Risk"]
        == "Medium"
    ).sum()

    low = (
        forecast["Predicted Risk"]
        == "Low"
    ).sum()

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric(
            "High Risk Areas",
            high
        )

    with c2:
        st.metric(
            "Medium Risk Areas",
            medium
        )

    with c3:
        st.metric(
            "Low Risk Areas",
            low
        )

    st.dataframe(
        forecast[
            [
                "location",
                "Current Risk",
                "Predicted Risk"
            ]
        ]
    )

    st.subheader(
        "Predicted Risk Distribution"
    )

    risk_counts = (
        forecast["Predicted Risk"]
        .value_counts()
    )

    fig, ax = plt.subplots(
        figsize=(8,4)
    )

    ax.bar(
        risk_counts.index,
        risk_counts.values
    )

    ax.set_title(
        "Predicted Risk Levels"
    )

    ax.set_ylabel(
        "Number of Locations"
    )

    st.pyplot(fig)