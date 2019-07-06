import pandas as pd
import numpy as np
from settings import *
import logging


def load_qdata_csv() -> pd.DataFrame:
    """
    Read the csv containing the question data into the programme database.

    Note:
    This is only suitable for a proof-of-concept software. In the later version when we have a large number of data,
    we cannot afford to read this into the RAM every time so more sophisticated data-base housekeeping would be required

    Input CSV should be of the following format:
    Year | Question Number | Yr_Qn (question unique identifier) | Category | Label | Difficulty level (1-5) | Solution

    This def also adds the topic (the single-digit identifier), which may encompass more than one category.
    :return:
    """
    raw_data = pd.read_csv(QUESTION_DATA_PATH)
    cols_to_check = ['Yr_Qn_No', 'Label', 'Difficulty', 'Soln']
    assert all([col in raw_data.columns for col in cols_to_check]), \
        "One or more required column is not in the csv file supplied!"
    df = raw_data[cols_to_check]
    # Pre-process the csv data by adding relevant columns
    if 'Topic' not in raw_data.columns:
        df['Topic'] = df['Label'].str[:1]

    # Add in accuracy data - initialise to nan
    if 'Accuracy' not in raw_data.column:
        df['Accuracy'] = np.nan
    return df


def load_user_data_csv() -> pd.DataFrame:
    """
    Load the user data into a pandas dataframe
    :return:
    """
    try:
        raw_data = pd.read_csv(USER_DATA_PATH)
    except FileNotFoundError:
        logging.warning(USER_DATA_PATH + " is not found or cannot be opened. Create a new user data file at " +
                        USER_DATA_PATH)
        raw_data = None

    # Sanity checks
    if raw_data is not None:
        assert 'User_ID' in raw_data.columns, "User_ID column is required for the user data file!"
        df = raw_data
    else:
        # Create a new user data *file*
        pass

    return df


def save_qdata_csv(qdata: pd.DataFrame):
    """
    Save the question data (which may be modified in this session) into non-volatile csv file.
    :param qdata:
    :return:
    """
    qdata.to_csv(QUESTION_DATA_PATH)


def save_user_data_csv(user_data: pd.DataFrame):
    """
    Save the user data which may be modified in this session into non-volatile csv file.
    :param user_data:
    :return:
    """
    user_data.to_csv(USER_DATA_PATH)


def clear_screen():
    """
    Clear the display of Python console
    :return:
    """
    from os import system, name

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


# For testing purposes only - this code block should not be run in usual mode of operation of the software
if __name__ == "__main__":
    load_qdata_csv()