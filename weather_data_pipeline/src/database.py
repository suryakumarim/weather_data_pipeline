import sqlite3
from config.config import DATABASE_PATH

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        city_id INTEGER PRIMARY KEY,
        city_name TEXT NOT NULL,
        country TEXT,
        latitude REAL,
        longitude REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        record_id INTEGER PRIMARY KEY,
        city_id INTEGER,
        timestamp TIMESTAMP,
        temperature_c REAL,
        humidity INTEGER,
        pressure_hpa REAL,
        wind_speed_mps REAL,
        weather_condition TEXT,
        FOREIGN KEY (city_id) REFERENCES cities(city_id)
    )
    ''')
    conn.commit()
    conn.close()
