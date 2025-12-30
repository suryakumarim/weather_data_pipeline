from database import get_connection
from api_client import fetch_weather
from config.config import CITIES

def run_etl():
    conn = get_connection()
    cursor = conn.cursor()
    for city in CITIES:
        data = fetch_weather(city)
        if data:
            cursor.execute("INSERT OR IGNORE INTO cities (city_name) VALUES (?)", (city,))
            cursor.execute("SELECT city_id FROM cities WHERE city_name=?", (city,))
            city_id = cursor.fetchone()[0]
            cursor.execute('''
            INSERT INTO weather_data
            (city_id, timestamp, temperature_c, humidity, pressure_hpa, wind_speed_mps, weather_condition)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (city_id, data['timestamp'], data['temperature'], data['humidity'], data['pressure'],
             data['wind_speed'], data['condition']))
    conn.commit()
    conn.close()
