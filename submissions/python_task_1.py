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



def get_type_count(df: pd.DataFrame) -> dict:
  """
  Categorizes 'car' values into types and returns a dictionary of counts.

  Args:
      df (pandas.DataFrame)

  Returns:
      dict: A dictionary with car types as keys and their counts as values.
  """
  # Add a new categorical column 'car_type' based on values of the column 'car'
  df['car_type'] = pd.cut(df['car'], bins=[0, 15, 25, df['car'].max() + 1], labels=['low', 'medium', 'high'])

  # Calculate the count of occurrences for each 'car_type' category
  type_count = df['car_type'].value_counts().to_dict()

  # Sort the dictionary alphabetically based on keys
  type_count = dict(sorted(type_count.items()))

  return type_count

# Read the CSV file from the URL
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
df = pd.read_csv(url)

# Call the function
type_count = get_type_count(df)
print(type_count)



def get_bus_indexes(df: pd.DataFrame) -> list:
 """
 Returns the indexes where the 'bus' values are greater than twice the mean value of the bus column in the DataFrame.

 Args:
     df (pandas.DataFrame)

 Returns:
     list: List of indexes where 'bus' values exceed twice the mean.
 """
 # Identify the indices where the 'bus' values are greater than twice the mean value of the 'bus' column
 bus_indices = df[df['bus'] > 2 * df['bus'].mean()].index.tolist()

 # Sort the list in ascending order
 bus_indices.sort()

 return bus_indices

# Read the CSV file from the URL
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
df = pd.read_csv(url)

# Call the function
bus_indices = get_bus_indexes(df)
print(bus_indices)


def filter_routes(df: pd.DataFrame) -> list:
 """
 Filters and returns routes with average 'truck' values greater than 7.

 Args:
    df (pandas.DataFrame)

 Returns:
    list: List of route names with average 'truck' values greater than 7.
 """
 # Filter routes with average 'truck' values greater than 7
 filtered_routes = df.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()

 # Sort the list in ascending order
 filtered_routes.sort()

 return filtered_routes

# Read the CSV file from the URL
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
df = pd.read_csv(url)

# Call the function
filtered_routes = filter_routes(df)
print(filtered_routes)


import numpy as np

def multiply_matrix(matrix: pd.DataFrame) -> pd.DataFrame:
 """
 Multiplies matrix values with custom conditions.

 Args:
    matrix (pandas.DataFrame)

 Returns:
    pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
 """
 # If a value in the DataFrame is greater than 20, multiply those values by 0.75
 # If a value is 20 or less, multiply those values by 1.25
 matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

 # Round the values to 1 decimal place
 matrix = matrix.round(1)

 return matrix

# Read the CSV file from the URL
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
df = pd.read_csv(url)

# Call the function
car_matrix = generate_car_matrix(df)
multiplied_matrix = multiply_matrix(car_matrix)
print(multiplied_matrix)


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
