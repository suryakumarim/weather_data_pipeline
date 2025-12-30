from database import get_connection

def check_missing_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM weather_data WHERE temperature_c IS NULL")
    missing = cursor.fetchone()[0]
    conn.close()
    return missing

def validate_temperature():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM weather_data WHERE temperature_c < -50 OR temperature_c > 60")
    outliers = cursor.fetchone()[0]
    conn.close()
    return outliers
