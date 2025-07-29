# aqi_utils.py
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAQ_API_KEY")
API_BASE = "https://api.openaq.org/v3"

def get_locations(country="IN", parameter="pm25", limit=100):
    """Fetch valid monitoring station locations by country and parameter"""
    try:
        url = f"{API_BASE}/locations"
        headers = {"X-API-Key": API_KEY} if API_KEY else {}
        params = {
            "country": country,
            "parameter": parameter,
            "limit": limit
        }
        r = requests.get(url, headers=headers, params=params, timeout=10)
        r.raise_for_status()
        return pd.DataFrame(r.json()["results"])
    except Exception as e:
        print(f"[ERROR] Failed to fetch locations: {e}")
        return pd.DataFrame()

def fetch_aqi_by_location(location_id, parameter="pm25", limit=100):
    """Fetch real-time AQI values by location_id"""
    try:
        url = f"{API_BASE}/measurements"
        headers = {"X-API-Key": API_KEY} if API_KEY else {}
        params = {
            "location_id": location_id,
            "parameter": parameter,
            "limit": limit,
            "sort": "desc"
        }
        r = requests.get(url, headers=headers, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()

        records = []
        for result in data.get("results", []):
            coords = result.get("coordinates", {})
            records.append({
                "location": result.get("location"),
                "parameter": result.get("parameter"),
                "value": result.get("value"),
                "unit": result.get("unit"),
                "timestamp": result.get("date", {}).get("local"),
                "lat": coords.get("latitude"),
                "lon": coords.get("longitude")
            })
        return pd.DataFrame(records)

    except Exception as e:
        print(f"[ERROR] Failed to fetch AQI data: {e}")
        return pd.DataFrame()
