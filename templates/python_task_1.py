import pandas as pd


import numpy as np

def generate_car_matrix(df: pd.DataFrame) -> pd.DataFrame:
   """
   Creates a DataFrame for id combinations.

   Args:
       df (pandas.DataFrame)

   Returns:
       pandas.DataFrame: Matrix generated with 'car' values, 
                        where 'id_1' and 'id_2' are used as indices and columns respectively.
   """
   # Set 'id_1' as the index of our DataFrame
   df = df.set_index('id_1')

   # Pivot our DataFrame to get the desired structure
   df = df.pivot(columns='id_2', values='car')

   # Set the diagonal values to 0
   np.fill_diagonal(df.values, 0)

   return df

# Read the CSV file from the URL
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
df = pd.read_csv(url)

# Call the function
car_matrix = generate_car_matrix(df)
print(car_matrix)


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here

    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here

    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
