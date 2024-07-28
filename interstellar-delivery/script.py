from datetime import datetime, timedelta


def format_date(timestamp: int, datetime_format: str) -> str:
    return datetime.fromtimestamp(timestamp).strftime(datetime_format)


def calculate_landing_time(rocket_launch_dt: datetime, travel_duration: int) -> str:
    return (rocket_launch_dt + timedelta(days=travel_duration)).strftime("%d-%m-%Y")


def days_until_delivery(expected_delivery_dt: datetime, current_dt: datetime) -> int:
    return (expected_delivery_dt - current_dt).days