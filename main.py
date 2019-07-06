# NeuAcademy Framework
# Author: Xingchen Wan
# Contact: xingchen.wan@outlook.com

import generator, discriminator
from utils import *
from initialisation import *
from settings import *


def main_loop():
    udata = load_user_data_csv()

    # Get all user ids
    uids = udata.iloc[:, 0]
    qdata = load_qdata_csv()

    # Some initialisation stuff and login
    while True:
        user_id = input("Welcome to NeuAcademy. Please enter your user ID to continue.")
        if user_id not in uids:
            create_new = input("User ID " + user_id +
                               " not found in our system. Would you like to create a new profile? Y to continue, "
                               "other key to abort.")
            if create_new == 'y' or create_new == 'Y':
                udata = init_user(udata)
            else: break

    clear_screen()

    # Select appropriate questions
    while True:
        topic = input("Please press label(s) corresponding to the topics you'd like to practice. "
                      "Use  ',' to separate different labels \n"
                      "Press H to get a list of topics. \n"
                      "Press ENTER to include all topics. ")
        if topic == 'H':
            for k, v in LABEL2CATEGORY.items():
                print("|" + str(k) + " : " + str(v) + "| \n")
        elif topic == '':
            sub_qdata = qdata
            break
        else:
            labels = topic.split(",")
            str_keys = [str(key) for key in LABEL2CATEGORY.keys()]
            try:
                assert all([label in str_keys for label in labels])
                sub_qdata = qdata[qdata['Label'] in labels]
                break
            except AssertionError:
                print("Some keys you entered are not in the list of topics. Try again.")

    # Do actual stuff - recommend questions to the user
    session_res = [] * NUM_QNS_PER_SESSION

    for i in range(NUM_QNS_PER_SESSION):
        q_id = generator.recommend_question(sub_qdata, user_id)
        qn_res = discriminator.get_response()

        # Store the user response in a repository that will be later used to display a session summary
        session_res[i] = qn_res
        score = discriminator.discriminate(qn_res, q_id, sub_qdata)
        discriminator.update_qn_data(score, q_id, qdata)
        discriminator.update_user_data(score, user_id, udata)

    # Update user and question database from the information we learnt from this session and close the current session
    clear_screen()
    print("Session completed! Here is your result")
    generator.generate_session_summary()
    save_user_data_csv(udata)
    save_qdata_csv(qdata)
    print("Thank you for using NeuAcademy. Session ended.")


if __name__ == '__main__':
    main_loop()