from datetime import datetime, timedelta


def format_date(timestamp: int, datetime_format: str) -> str:
    """Convert timestamp to a readable datetime string.

    Args:
      timestamp: int: Unix timestamp integer.
      datetime_format: str: Desired date format.

    Returns:
      str: Date in string format.
    """
    return datetime.fromtimestamp(timestamp).strftime(datetime_format)


def calculate_landing_time(rocket_launch_dt: datetime, travel_duration: int) -> str:
    """Calculate estimated landing time.

    Args:
      rocket_launch_dt: datetime: Time of rocket launch.
      travel_duration: int: Expected travel time in days.

    Returns:
      str: Estimated Mars landing time in format DD-MM-YYYY.
    """
    return (rocket_launch_dt + timedelta(days=travel_duration)).strftime("%d-%m-%Y")


def days_until_delivery(expected_delivery_dt: datetime, current_dt: datetime) -> int:
    """Calculate the days until a package arrives.

    Args:
      expected_delivery_dt: datetime: Estimate package delivery time.
      current_dt: datetime: Current time and date.

    Returns:
      int: Days remaining until delivery.
    """
    return (expected_delivery_dt - current_dt).days
