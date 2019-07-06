# NeuAcademy Framework
# Author: Xingchen Wan
# Contact: xingchen.wan@outlook.com

import pandas as pd
import numpy as np


def recommend_question(qdata: pd.DataFrame, u_id):
    """
    Recommend questions for the specific user
    :param qdata: question data. Needs to be a pandas dataframe
    :param u_id: user id
    :return: the question identifier string from which the user may retrieve the actual question
    """
    pass


def get_question_information(qdata: pd.DataFrame, q_id: str):
    """
    Get relevant question information for the help of the user. Example information may include
    (frequency of the question in past year papers, historical accuracy rate by other users and etc). We may add or
    remove information as we may see fit
    :param qdata:
    :param q_id:
    :return:
    """
    pass


def generate_session_summary():
    """
    Generate a session summary that shows the user's performance in the previous session. Some metrics may include:
    1. Accuracy rate: out of all questions, how many did the users get right or wrong?
    2. Speed: how much time the user spent on each question (or each type of question).
    3. Some customised feedback we would like to give ("e.g. strong in statics - keep it up. weak in probability - needs
    more practice). etc.
    :return:
    """
    pass