import pandas as pd
from database import get_connection

def generate_report():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM weather_data", conn)
    conn.close()
    df.describe().to_csv("../reports/weather_summary.csv")
    print("Report generated at reports/weather_summary.csv")
