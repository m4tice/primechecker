# pylint: disable=line-too-long
"""Test ultilities"""

import pandas as pd

from src.utils.util import get_none
from src.utils.util import get_account_numbers_by_id
# from src.utils.utils import get_account_numbers_by_sample


from tests.test_settings import TEST_FILE_PATH
from tests.test_settings import TEST_BM_NUMBER_EXTRACT_RQ1ID_01, TEST_BM_NUMBER_EXTRACT_RQ1ID_02, TEST_BM_NUMBER_EXTRACT_RQ1ID_03
from tests.test_settings import TEST_BM_NUMBER_EXTRACT_RESULT_01, TEST_BM_NUMBER_EXTRACT_RESULT_02, TEST_BM_NUMBER_EXTRACT_RESULT_03


test_data = pd.read_excel(TEST_FILE_PATH)
test_data = test_data.set_index("id")


def test_get_none():
    """
    Assert get_none()
    Expected return of get_none() is 'None'
    """
    assert get_none() is None


def test_get_account_numbers_by_id():
    """
    Expectation: function is able to filter BM numbers
    from input of data frame using RQ1ID
    """
    assert get_account_numbers_by_id(test_data, TEST_BM_NUMBER_EXTRACT_RQ1ID_01) == TEST_BM_NUMBER_EXTRACT_RESULT_01
    assert get_account_numbers_by_id(test_data, TEST_BM_NUMBER_EXTRACT_RQ1ID_02) == TEST_BM_NUMBER_EXTRACT_RESULT_02
    assert get_account_numbers_by_id(test_data, TEST_BM_NUMBER_EXTRACT_RQ1ID_03) == TEST_BM_NUMBER_EXTRACT_RESULT_03
    # print(get_account_numbers_by_id(test_data, TEST_BM_NUMBER_EXTRACT_RQ1ID_01))


def test_get_account_numbers_by_sample():
    """
    Expectation: function is able to filter BM numbers
    from input of data frame using sample input string
    """


test_get_account_numbers_by_id()
