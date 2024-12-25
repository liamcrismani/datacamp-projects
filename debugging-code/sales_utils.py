import pandas as pd


#TODO: add try except
def get_quantity_ordered_sum(sales_quantity_ordered: pd.core.series.Series) -> int:
    """Calculates the total sum on the 'quantity_ordered' column.

    Args:
        sales_quantity_ordered (pd.core.series.Series): The pandas Series for the 'quantity_ordered' column.

    Returns:
        total_quantity_ordered (int): The total sum of the 'quantity_ordered' column.
    """

    total_quantity_ordered = 0
    for quantity in sales_quantity_ordered:
        total_quantity_ordered += quantity
    return total_quantity_ordered

#TODO: Add try except block
def get_price_each_average(sales_price_each, num_places=2):
    """Calculates the average on the 'price_each' column
       using pandas built in methods and rounds to the desired number of places.

    Args:
        sales_price_each (pd.core.series.Series): The pandas Series for the 'price_each' column.
        num_of_places (int): The number of decimal places to round.

    Returns:
        average_price_each (float): The average of the 'price_each' column.
    """

    total_of_price_each = sales_price_each.sum()
    len_of_price_each = len(sales_price_each)
    average_price_each = round(
        total_of_price_each / len_of_price_each, num_places
    )
    return average_price_each
