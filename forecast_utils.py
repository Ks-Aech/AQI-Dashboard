# forecast_utils.py
from prophet import Prophet
import pandas as pd

def forecast_aqi(df, days=3):
    try:
        df = df[["timestamp", "value"]].copy()
        df.rename(columns={"timestamp": "ds", "value": "y"}, inplace=True)
        df["ds"] = pd.to_datetime(df["ds"])

        model = Prophet(daily_seasonality=True)
        model.fit(df)

        future = model.make_future_dataframe(periods=days)
        forecast = model.predict(future)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
    except Exception as e:
        print(f"[ERROR] Forecast failed: {e}")
        return pd.DataFrame()
