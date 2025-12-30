import requests
from datetime import datetime
from config.config import API_KEY

def fetch_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return {
            'city': city,
            'timestamp': datetime.now(),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'condition': data['weather'][0]['description']
        }
    except requests.exceptions.RequestException as e:
        print(f"API Error for {city}: {e}")
        return None
