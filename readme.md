# 🌫️ Real-Time AQI Monitoring and Forecasting Dashboard

An interactive, modern dashboard to monitor real-time Air Quality Index (AQI) levels across India, built with **Streamlit**, **OpenAQ API v3**, **Folium maps**, **Prophet forecasting**, and **Gmail email alerts**.

---

## 🚀 Features

- 🌍 **Real-Time AQI Monitoring** via [OpenAQ v3 API](https://docs.openaq.org/)
- 📍 **Location-aware Monitoring Stations** (by `location_id`)
- 🔮 **Time-Series Forecasting** using Facebook Prophet
- 🗘️ **Interactive AQI Map** with Folium and severity coloring
- 📧 **Email Alerts** via Gmail API for dangerous AQI levels
- 🧼 Modern UI using Streamlit + Plotly + Folium


---

## 🧱 Tech Stack

| Layer         | Tools Used                    |
| ------------- | ----------------------------- |
| Frontend      | Streamlit, Plotly, Folium     |
| Backend       | Python, Prophet, Pandas       |
| APIs          | OpenAQ API v3, Gmail API      |
| Auth & Config | `.env` (dotenv), Gmail OAuth2 |

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/aqi-dashboard.git
cd aqi-dashboard
```

### 2️⃣ Create `.env` File

```env
OPENAQ_API_KEY=your_openaq_api_key_here
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Gmail API for Email Alerts

- Create a project at [Google Cloud Console](https://console.cloud.google.com/)
- Enable **Gmail API**
- Download `credentials.json` to the root folder
- Run:

```bash
python gmail_auth.py
```

- Authenticate → `token.pkl` will be saved

---

### 5️⃣ Run the Dashboard

```bash
streamlit run app.py
```

---

## ⚙️ Project Structure

```
aqi_dashboard/
├── app.py
├── aqi_utils.py
├── forecast_utils.py
├── map_utils.py
├── email_alert.py
├── gmail_auth.py
├── requirements.txt
├── .env
├── credentials.json
└── README.md
```

---

## 🧪 Sample Data Flow

1. User selects a pollutant and location from sidebar
2. Data fetched from OpenAQ by `location_id`
3. Interactive chart and forecast are rendered
4. Folium map visualizes station-level pollution
5. Optional alert emails are triggered if AQI > 150

---

## 📬 Contact

**Author**: [Mohd Khalid Shaikh](https://github.com/Ks-Aech)\
**LinkedIn**: [linkedin.com/in/mohd-khalid-shaikh-a0a3aa30a](https://www.linkedin.com/in/mohd-khalid-shaikh-a0a3aa30a/)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

```
```
