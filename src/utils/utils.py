"""Ultilities"""

import pandas as pd

from utils.settings import KEYWORD_BM, BM_NUMBER_LEN


def get_none():
    """
    This function return None
    Its purpose is for pytest GitHub Actions demo
    """
    return None


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
