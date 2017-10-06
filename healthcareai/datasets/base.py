"""Dataset loading utilities."""

import os
import pandas as pd


def load_data(data_file_name):
    """Load data from module_path/data/data_file_name.

    Args:
        data_file_name (str) : Name of csv file to be loaded from
        module_path/data/data_file_name. Example: 'diabetes.csv'

    Returns:
        Pandas.core.frame.DataFrame: A pandas dataframe

    Examples:
        >>> load_data('diabetes.csv')
    """
    file_path = os.path.join(os.path.dirname(__file__), 'data', data_file_name)

    return pd.read_csv(file_path, na_values=['None'])


def load_diabetes():
    """Load and return the diabetes dataset."""
    return load_data('diabetes.csv')


def load_dermatology():
    """
    Load a dermatology dataset for multi class classification.

    Dataset from http://archive.ics.uci.edu/ml/datasets/dermatology

    Note: the dataset contains two columns named `target_str` and `target_num`.
        `target_str` contains strings, e.g. 'one', 'two', 'three', ...
        `target_num` contains numbers, e.g. 1, 2, 3, ...
        Choose one variable as a classification outcome and drop the other one.
    """
    return load_data('dermatology_multiclass_data.csv')
