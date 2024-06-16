import pytest
from script import nutritional_summary

@pytest.fixture
def prepare_data():
    data = {"Croissants, cheese": 150, "Orange juice, raw": 250}
    return data

def test_nutritional_summary(prepare_data):
    goal = {'calories': 733.5, 'total_fat': 32.0, 'protein': 15.55,
        'carbohydrate': 96.5, 'sugars': 38.025}
    nutritional_summary(prepare_data)
    global result
    assert result.keys() == goal.keys()
    assert result.values() == goal.values()
