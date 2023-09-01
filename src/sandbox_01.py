"""Sandbox for testing. Should be deleted when released officially"""


import pandas as pd

from utils.utils import get_account_numbers_by_id, get_account_numbers_by_sample
from utils.settings import RQONE_FILE_PATH


rqone_data = pd.read_excel(RQONE_FILE_PATH)

print(rqone_data)
