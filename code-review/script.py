import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def prepare_smartphone_data(file_path):
    """
    Prepare smartphone data for visualization.
        - read csv to DataFrame
        - reducing the number of columns to only those needed for analysis
        - removing records without a battery_capacity value
        - divide the price column by 100 to find the dollar amount

    :param file_path: the file path where the raw smartphone data is stored
    :return: a cleaned dataset having had the operations above applied to it
    """
    if os.path.exists(file_path):
        rawData = pd.read_csv(file_path)
    else:
        raise Exception(f"File containing data not found at path {file_path}")

    columns_to_keep = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size"
        ]

    trimmedData = rawData.loc[:, columns_to_keep]

    # Remove records without a battery_capacity value
    reducedData = trimmedData.dropna(subset=["battery_capacity", "os"])

    # Divide the price column by 100 to find the dollar amount
    reducedData["price"] = reducedData["price"] / 100

    return reducedData


def column_to_label(column_name):
    """
    Convert a column name in a pandas DataFrame to a string that can be
    used as a label in a plot.
    
    :param column_name: string containing original column name
    :return: string that is ready to be presented on a plot
    """
    # Validate that column_name is a string
    if isinstance(column_name, str):
        return " ".join(column_name.split("_")).title()
    
    # If the value provided is not a string, raise an Exception
    else:
        raise Exception("Please makes sure to pass a value of type 'str'.")


def visualize_versus_price(clean_data, x):
    """
    Use seaborn and matplotlib to identify a pattern between avg_rating and 
    battery_capacity.
    
    :param clean_data: a pandas DataFrame containing cleaned smartphone data
    :param x: variable to be plotted on the x-axis
    :return: None
    """
    # Create the scatterplot
    sns.scatterplot(x=x, y="price", data=clean_data, hue="os")
    
    # Add x and y labels
    plt.xlabel(column_to_label(x))
    plt.ylabel("Price ($)")
    
    # Add a title to the plot
    plt.title(f"{column_to_label(x)} vs. Price")
    
    
# Call the function
cleaned_data = prepare_smartphone_data("./data/smartphones.csv")

# Call the visualize_versus_price function
visualize_versus_price(cleaned_data, "processor_speed")