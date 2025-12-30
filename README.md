# Weather Data Pipeline System

## Project Overview
End-to-end ETL pipeline that extracts weather data from OpenWeatherMap API, transforms and stores it in a SQLite database, performs data validation, and generates automated reports.

## Folder Structure
- config/ → API keys and settings
- src/ → Python modules
- database/ → SQLite database
- scripts/ → Run pipeline scripts
- logs/ → ETL logs
- reports/ → Generated reports
- tests/ → Unit and integration tests

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Setup database:
   python src/database.py
3. Run ETL manually:
   python scripts/run_etl.py
4. Start automated scheduler:
   python src/scheduler.py
5. Generate reports:
   python src/reporter.py
6. Monitor system:
   python src/monitor.py
