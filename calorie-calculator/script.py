import json  # Import the json module to work with JSON files

# Open the nutrition.json in read mode and load its content into dictionary
with open('nutrition.json', 'r') as json_file:
    nutrition_dict = json.load(json_file)  # Load JSON content into dictionary


def nutritional_summary(food_dict: dict) -> dict:
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
    result = {'calories': 0, 'total_fat': 0, 'protein': 0, 'carbohydrate': 0, 
              'sugars': 0}
    
    # Process each food item.
    for food in food_dict.items():
   
        if food[0] in nutrition_dict.keys():
            # Calculate nutrional values
            result['calories'] += round(food[1]/100 * nutrition_dict.get(food[0])['calories'], 2)
            result['total_fat'] += round(food[1]/100 * nutrition_dict.get(food[0])['total_fat'], 2)
            result['protein'] += round(food[1]/100 * nutrition_dict.get(food[0])['protein'], 2)
            result['carbohydrate'] += round(food[1]/100 * nutrition_dict.get(food[0])['carbohydrate'], 2)
            result['sugars'] += round(food[1]/100 * nutrition_dict.get(food[0])['sugars'], 2)
        
        elif food[0] not in nutrition_dict.keys():
            result = food[0]
            break
    
    return result


print(nutritional_summary({"Croissant": 150, "Orange juice": 250}))
