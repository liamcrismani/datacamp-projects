from script import nutritional_summary

def test_nutritional_summary(food_dict: dict) -> None:
    """
      Summary of nutritional info from all foods in food_dict.
        E.g {'calories': 733.5, 'total_fat': 32.0, 'protein': 15.55,
        'carbohydrate': 96.5, 'sugars': 38.025}
    """
    goal = {'calories': 733.5, 'total_fat': 32.0, 'protein': 15.55,
        'carbohydrate': 96.5, 'sugars': 38.025}
    nutritional_summary({"Croissants, cheese": 150, "Orange juice, raw": 250}) 
    assert result.keys() == goal.keys()
    assert result.values() == goal.values()
