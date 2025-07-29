### app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_folium import folium_static
from aqi_utils import get_locations, fetch_aqi_by_location
from forecast_utils import forecast_aqi
from map_utils import generate_map
from email_alert import send_email

st.set_page_config(page_title="🌍 AQI Dashboard", layout="wide")
st.title("🌫️ Real-Time AQI Monitoring & Forecasting")

# Sidebar config
with st.sidebar:
    st.header("Configuration")
    parameter = st.selectbox("Select Pollutant", ["pm25", "pm10", "co", "no2", "so2"])
    locations_df = get_locations(country="IN", parameter=parameter)
    if locations_df.empty:
        st.error("No monitoring stations found.")
    else:
        location_name = st.selectbox("Monitoring Station", locations_df["name"].unique())
        selected_id = locations_df[locations_df["name"] == location_name]["id"].iloc[0]
        forecast_days = st.slider("Forecast Days", 1, 7, 3)
        email = st.text_input("Email for Alerts")

# Main app
if locations_df.empty:
    st.stop()

# Fetch data by location_id
df = fetch_aqi_by_location(location_id=selected_id, parameter=parameter)

if df.empty:
    st.warning("No AQI data available for this station.")
else:
    st.subheader(f"📊 {parameter.upper()} Levels at {location_name}")
    st.dataframe(df.head())

    fig = px.line(df.sort_values("timestamp"), x="timestamp", y="value",
                  title=f"{parameter.upper()} Trend at {location_name}", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔮 AQI Forecast")
    forecast = forecast_aqi(df, forecast_days)
    st.line_chart(forecast.set_index("ds")["yhat"])

    st.subheader("🗺️ AQI Map")
    folium_static(generate_map(df))

    st.subheader("📧 Email Alert")
    if st.button("Send Alert if AQI > 150") and email:
        high = df[df["value"] > 150]
        if not high.empty:
            for _, row in high.iterrows():
                send_email("AQI Alert 🚨", f"{row['parameter'].upper()} at {row['location']} is {row['value']}.", email)
            st.success("Alert sent!")
        else:
            st.info("AQI levels are safe.")
