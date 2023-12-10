import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Ensure 'id_start', 'id_end', and 'distance' columns are present
    if 'id_start' not in df.columns or 'id_end' not in df.columns or 'distance' not in df.columns:
        raise ValueError("Input dataset is missing required columns.")

    # Create a pivot table to get bidirectional distances
    distance_matrix = df.pivot(index='id_start', columns='id_end', values='distance').fillna(0)

    # Make the matrix symmetric
    distance_matrix = distance_matrix + distance_matrix.T

    # Set diagonal values to 0
    distance_matrix.values[[range(len(distance_matrix))]*2] = 0

    return distance_matrix

# Load the dataset from the provided GitHub URL
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-3.csv'
dataset = pd.read_csv(url)

# Call the function with the dataset
result_distance_matrix = calculate_distance_matrix(dataset)
print(result_distance_matrix)

    return df


def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Ensure the input is a valid DataFrame
    if not isinstance(distance_matrix, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    # Reshape the distance matrix to long format
    unrolled_df = distance_matrix.stack().reset_index()
    unrolled_df.columns = ['id_start', 'id_end', 'distance']

    # Exclude rows where id_start is equal to id_end
    unrolled_df = unrolled_df[unrolled_df['id_start'] != unrolled_df['id_end']]

    return unrolled_df

# Call the function with the distance matrix from Question 1
result_unrolled_df = unroll_distance_matrix(result_distance_matrix)
print(result_unrolled_df)

    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Ensure the input is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    # Filter DataFrame based on the reference_id
    reference_data = df[df['id_start'] == reference_id]

    # Calculate the average distance for the reference_id
    reference_avg_distance = reference_data['distance'].mean()

    # Calculate the percentage threshold
    threshold = 0.1  # 10%

    # Find IDs within the percentage threshold
    result_series = df.groupby('id_start')['distance'].mean()
    result_series = result_series[(result_series >= (1 - threshold) * reference_avg_distance) &
                                  (result_series <= (1 + threshold) * reference_avg_distance)]

    # Sort the result Series by average distance
    result_series = result_series.sort_values()

    return result_series

# Call the function with the unrolled DataFrame from Question 2 and a reference ID
reference_id = 1  # Replace with the desired reference ID
result_within_threshold = find_ids_within_ten_percentage_threshold(result_unrolled_df, reference_id)
print(result_within_threshold)
    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Ensure the input is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    # Define rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Add columns for toll rates based on vehicle type
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate_coefficient

    return df

# Call the function with the unrolled DataFrame from Question 2
result_with_toll_rates = calculate_toll_rate(result_unrolled_df)
print(result_with_toll_rates)

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df
