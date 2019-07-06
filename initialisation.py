# Initialisation routine for first time login of an user

import pandas as pd
import numpy as np
from settings import *
from utils import *


def init_user(udata: pd.DataFrame) -> pd.DataFrame:
    """
    Initialise a new user in the system
    :param udata: the user data df
    :return: the updated user data df containing the new information
    """

    user_data = pd.Series(0, index=udata.columns)

    while True:
        user_id = input("Welcome to NeuAcademy v.1. Please enter your preferred ID: ")
        if user_id in udata['ID']:
            print("ID " + user_id + " already exists. Choose another ID")
        else:
            user_data['ID'] = user_id
            break

    while True:
        try:
            level = int(input("Select your syllabus: \n Physics Aptitude Test (PAT): 1"))
            break
        except ValueError:
            print("Please enter an integer number.")

    if level == 1:
        print("Syllabus PAT selected.")
        response = generate_pat_questionnaire()

        # Update user profile using the response to the initial questionnaire
        udata = update_user_profile_from_questionnaire(user_data, response)

    else: # This will be updated when we have question data for other syllabi
        print("Syllabus" + str(level) + "not currently available.")

    save_user_data_csv(udata)
    return udata


def generate_pat_questionnaire() -> list:
    """
    Generate survey question for each and every PAT topic.
    :return: A list of integers (length = number of PAT topics) in the range of [1,5] which gauges the self-assessed
    ability of the student in each topic.
    """
    print("The next few questions are intended to survey your understanding across five broad categories of the PAT"
          "syllabus. On a scale of 1 (least understanding) to 5 (best understanding), select your response.")
    responses = [0] * NUM_PAT_TOPICS

    for i in range(NUM_PAT_TOPICS):
        while True:
            try:
                responses[i] = int(input("Enter an integer from 1 to 5 for"+ PAT_TOPICS[i] + ": "))
                if responses[i] >= 1 and responses[i] <= 5:
                    break
                else:
                    print("Please enter an integer between 1 to 5")
            except ValueError:
                print("Please enter an integer number.")
    return responses


def update_user_profile_from_questionnaire(user_id: pd.Series, responses: list) -> pd.DataFrame:
    """
    Update user profile from the questionnaire response
    :param user_data: data of the single user presented as a pandas series
    :param responses: responses from the questionnaire - a list by default
    todo: we have to design an algorithm that assigns appropriate weight to this initial questionnnaire!
    :return: a new userdata dataframe that contains the updated information about this user
    """
    pass

