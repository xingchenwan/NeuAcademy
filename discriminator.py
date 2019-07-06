import pandas as pd
import numpy as np
import time


def get_response() -> list:
    """
    Get response from the user about a particular question. It also computes the time user took to complete the qn.
    :return:
    """
    t0 = time.time()
    soln = input("Please enter your response to the question above.")
    t1 = time.time()
    return [soln, t1 - t0]


def discriminate(user_response: list, q_id: str, qdata: pd.DataFrame):
    """
    Compare the user solution to the true solution. This also includes metrics such as the comparison of time, etc.
    :param user_response: the response give by the user
    :param q_id: the identifier string of the question in interest
    :param qdata: the question data dataframe
    :return: a score, or an object that we will use to update the question and user data later. (Data type not yet
    determined here)
    todo: Specify the format the discriminate function returns
    """
    pass


def update_user_data(score, u_id: str, udata: pd.DataFrame) -> pd.DataFrame:
    """
    Update the user database
    :param score: the object returned by function "discriminate"
    :param u_id: the user identifier string
    :param udata: userdata dataframe
    :return: the new udata dataframe
    """
    pass


def update_qn_data(score, q_id: str, qdata: pd.DataFrame) -> pd.DataFrame:
    """
    Update the question database
    :param score: the object returned by function "discriminate"
    :param q_id: the question identifier string
    :param qdata: question dataframe
    :return: question dataframe
    """
    pass