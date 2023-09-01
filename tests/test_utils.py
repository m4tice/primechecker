"""Test ultilities"""

import pandas as pd

from src.utils.utils import get_none
from src.utils.utils import get_account_numbers_by_id
from src.utils.utils import get_account_numbers_by_sample


def test_get_none():
    """
    Assert get_none()
    Expected return of get_none() is 'None'
    """
    assert get_none() is None


def test_get_account_numbers_by_id(data_frame: pd.DataFrame, rq1id: str):
    """
    Expectation: function is able to filter BM numbers
    from input of data frame using RQ1ID
    """
    pass


def test_get_account_numbers_by_sample(input_string: str):
    """
    Expectation: function is able to filter BM numbers
    from input of data frame using sample input string
    """
    pass
