"""Ultilities"""

import sys
import pandas as pd

sys.path.append("")

from src.utils.settings import KEYWORD_BM, BM_NUMBER_LEN  # work with GitHub Action Pytest  # pylint: disable=wrong-import-position
# from utils.settings import KEYWORD_BM, BM_NUMBER_LEN  # work locally


def get_none():
    """
    This function return None
    Its purpose is for pytest GitHub Actions demo
    """
    return None


def load_rqone_data(data_path: str):
    """
    load data from file and set id as index
    """
    data = pd.read_excel(data_path, index_col="id")
    return data


def get_account_numbers_by_id(data_frame: pd.DataFrame, rq1id: str):
    """
    get account numbers from dataframe with id
    """
    sample = data_frame.loc[rq1id]['AccountNumbers']

    if KEYWORD_BM in sample:
        sample_split = sample.split("\n")
        account_numbers = [item[item.find("BM"):item.find("BM") + BM_NUMBER_LEN] \
                        for item in sample_split if item != '']

        return account_numbers

    return "-"


def get_account_numbers_by_sample(input_string: str):
    """
    get account numbers from input string
    """

    if KEYWORD_BM in input_string:
        sample_split = input_string.split("\n")
        account_numbers = [item[item.find("BM"):item.find("BM") + BM_NUMBER_LEN] \
                        for item in sample_split if item != '']

        return account_numbers

    return "-"


def unzip_prime_datarow(data_row):
    """
    unzip_prime_datarow
    """
    try:
        task_name = str(data_row["Task Name/Description"])
        name = str(data_row["Name"])
        percentage_work = str(data_row["% Work Complete"]).split("%", maxsplit=1)[0]
        total_work = str(data_row["Work"]).split("h", maxsplit=1)[0]
        actual_work = str(data_row["Actual Work"]).split("h", maxsplit=1)[0]
        remaining_work = str(data_row["Remaining Work"]).split("h", maxsplit=1)[0]

        return task_name, name, percentage_work, total_work, actual_work, remaining_work

    except IndexError:
        return None


def unzip_rqone_datarow(data_row):
    """
    unzip_rqone_datarow
    """
    try:
        id = str(data_row["id"])  # pylint: disable=redefined-builtin, invalid-name
        title = str(data_row["Title"])
        life_cycle_state = str(data_row["LifeCycleState"])
        submitter = str(data_row["Submitter"])
        submit_date = str(data_row["SubmitDate"])
        account_numbers = get_account_numbers_by_sample(str(data_row["AccountNumbers"]))
        estimated_effort = str(data_row["EstimatedEffort"])
        allocation = str(data_row["Allocation"])
        category = str(data_row["Category"])
        assignee = str(data_row["Assignee.login_name"])

        return id, title, life_cycle_state, submitter, submit_date, account_numbers, \
            estimated_effort, allocation, category, assignee

    except KeyError:
        return None


def is_rq1id_duplicated(data_frame: pd.DataFrame, rq1id: str):
    """
    check if rq1 id is duplicated in dataframe
    """
    return data_frame.index.value_counts(rq1id).loc[rq1id] * 100 > 1


def rq1id_exist(data_frame: pd.DataFrame, rq1id: str):
    """
    check if rq1 ID exists in dataframe
    """
    return rq1id in data_frame.index.unique()


def clean_prime_data(data_frame: pd.DataFrame):
    """
    transform Prime data
    """
    transformed_prime_data_list = []
    key_word = "RQONE"

    for _, row in data_frame.iterrows():
        task_name, name, percentage_work,\
            total_work, actual_work, remaining_work = unzip_prime_datarow(row)

        # look for ones with RQONE ID
        if key_word in task_name:
            rqone_id = str(row["Task Name/Description"]).split("_", maxsplit=1)[0]
            task_name = str(row["Task Name/Description"]).split("_", maxsplit=1)[-1]
            transformed_prime_data_list.append([name,
                                    rqone_id,
                                    task_name,
                                    float(percentage_work),
                                    float(total_work),
                                    float(actual_work),
                                    float(remaining_work)])

    # create DataFrame from transformed prime data list
    transformed_prime_data_df = pd.DataFrame(transformed_prime_data_list,
                                         columns=["GroupName",
                                                  "ID",
                                                  "TaskName",
                                                  "Percentage",
                                                  "TotalWork",
                                                  "ActualWork",
                                                  "RemainWork"])

    transformed_prime_data_df = transformed_prime_data_df.set_index("ID")

    return transformed_prime_data_df
