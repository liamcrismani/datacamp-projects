import os
import pandas as pd


def prepare_smartphone_data(file_path):
    """
    Prepare smartphone data for visualization:
        - read csv to DataFrame
        - reducing the number of columns to only those needed for analysis
        - removing records without a battery_capacity value
        - divide the price column by 100 to find the dollar amount

    :param file_path: the file path where the raw smartphone data is stored
    :return: a cleaned dataset having had the operations above applied to it
    """
    # Load data
    if os.path.exists(file_path):
        rawData = pd.read_csv(file_path)
    else:
        raise Exception(f"File containing data not found at path {file_path}")

    # Define columns to keep
    columns_to_keep = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size"]

    trimmedData = rawData.loc[:, columns_to_keep]

    # Remove records without a battery_capacity value
    reducedData = trimmedData.dropna(subset=["battery_capacity", "os"])

    # Divide the price column by 100 to find the dollar amount
    reducedData["price"] = reducedData["price"] / 100

    return reducedData


# Call the function
cleaned_data = prepare_smartphone_data("./data/smartphones.csv")
