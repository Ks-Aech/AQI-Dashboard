# map_utils.py
import folium
import pandas as pd

def get_color(aqi):
    if aqi <= 50:
        return "green"
    elif aqi <= 100:
        return "yellow"
    elif aqi <= 150:
        return "orange"
    elif aqi <= 200:
        return "red"
    else:
        return "purple"

def generate_map(df):
    try:
        m = folium.Map(location=[20.59, 78.96], zoom_start=5)
        for _, row in df.iterrows():
            if pd.notna(row['lat']) and pd.notna(row['lon']):
                color = get_color(row['value'])
                folium.CircleMarker(
                    location=(row['lat'], row['lon']),
                    radius=8,
                    color=color,
                    fill=True,
                    fill_color=color,
                    fill_opacity=0.7,
                    popup=f"{row['location']}<br>{row['parameter'].upper()}: {row['value']} {row['unit']}"
                ).add_to(m)
        return m
    except Exception as e:
        print(f"[ERROR] Failed to generate map: {e}")
        return folium.Map(location=[20.59, 78.96], zoom_start=5)
