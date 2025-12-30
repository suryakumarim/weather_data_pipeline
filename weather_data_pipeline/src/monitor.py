from validators import check_missing_data, validate_temperature

def system_status():
    missing = check_missing_data()
    outliers = validate_temperature()
    print(f"Missing records: {missing}")
    print(f"Temperature outliers: {outliers}")
    if missing == 0 and outliers == 0:
        print("System Status: Healthy ✅")
    else:
        print("System Status: Issues detected ⚠️")

if __name__ == "__main__":
    system_status()
