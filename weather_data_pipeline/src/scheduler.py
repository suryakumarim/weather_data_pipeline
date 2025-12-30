import schedule
import time
from etl_pipeline import run_etl

schedule.every().hour.do(run_etl)  # Run every hour

while True:
    schedule.run_pending()
    time.sleep(1)
