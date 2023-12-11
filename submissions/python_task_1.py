import pandas as pd
import numpy as np
df=pd.read_csv('dataset-1.csv')

def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = car_matrix.fillna(0)
    for i in range(min(car_matrix.shape)):
        car_matrix.iloc[i, i] = 0
    df=car_matrix
    return df
generate_car_matrix(df)


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = np.select(conditions, choices, default='unknown')
    car_type_counts = df['car_type'].value_counts().to_dict()
    car_type_counts = sorted(car_type_counts.items())
    return dict(car_type_counts)
get_type_count(df)


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    mean_bus = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()
    bus_indexes.sort()
    
    return list(bus_indexes)
get_bus_indexes(df)


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    avg_truck_per_route = df.groupby('route')['truck'].mean()
    filtered_routes = avg_truck_per_route[avg_truck_per_route > 7]
    sorted_routes = filtered_routes.index.tolist()
    sorted_routes.sort()
    
    return list(sorted_routes)
filter_routes(df)


matrix=generate_car_matrix(df)
def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    modified_matrix = matrix.copy()
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_matrix = modified_matrix.round(1)
    
    return modified_matrix
multiply_matrix(matrix)


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
