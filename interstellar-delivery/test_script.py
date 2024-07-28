from datetime import datetime, timedelta
from scripts import format_date, calculate_landing_time, days_until_delivery

def test_format_date():
    date = format_date(1514665153, "%d-%m-%Y")
    assert date == "30-12-2017"


def test_calculate_landing_time():
    landing = calculate_landing_time(datetime(2023, 2, 15), 20)
    assert landing == "07-03-2023"


def test_days_until_delivery():
    days_remaining = days_until_delivery(datetime(2023, 2, 15), datetime(2023, 2, 5))
    assert days_remaining == 10

