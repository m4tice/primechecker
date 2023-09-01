# pylint: skip-file
"""Sandbox for testing. Should be deleted when released officially"""


import pandas as pd

from utils.util import get_account_numbers_by_id, get_account_numbers_by_sample
from utils.settings import RQONE_FILE_PATH


TEST_BM_NUMBER_EXTRACT_RQ1ID_01 = "RQONE02218228"
TEST_BM_NUMBER_EXTRACT_RQ1ID_02 = "RQONE03133330"
TEST_BM_NUMBER_EXTRACT_RQ1ID_03 = "RQONE03454099"


rqone_data = pd.read_excel(RQONE_FILE_PATH)
rqone_data = rqone_data.set_index("id")

accountnumbers = get_account_numbers_by_id(rqone_data, TEST_BM_NUMBER_EXTRACT_RQ1ID_03)
print(accountnumbers)
