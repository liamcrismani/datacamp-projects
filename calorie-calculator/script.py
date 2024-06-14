import json  # Import the json module to work with JSON files

# Open the nutrition.json in read mode and load its content into dictionary
with open('nutrition.json', 'r') as json_file:
    nutrition_dict = json.load(json_file)  # Load JSON content into dictionary


def nutritional_summary(food_dict: dict) -> None:
    """
    Calculates total nutritional summary for given food and quantity

    Parameters
    ----------
    food_dict: dict[str, float]
        Key is name food, value is amount in grams.
        E.g. {"Croissants, cheese": 150, "Orange juice, raw": 250}

    Returns
    -------
    dict
        Summary of nutritional info from all foods in food_dict.
        E.g {'calories': 733.5, 'total_fat': 32.0, 'protein': 15.55,
        'carbohydrate': 96.5, 'sugars': 38.025}
    """

    # Initialise result.
    result = {}

    # Process each food item.
    for food in food_dict.keys():

        # Handle non-existant food items.
        if food not in nutrition_dict.keys():
            print(food)

        else:
            # Calculate nutrional values.
            print(5)
