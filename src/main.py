"""main application"""

import os
import pandas as pd

from utils.settings import PRIME_FILE_PATH, RQONE_FILE_PATH
from utils.util import clean_prime_data, unzip_rqone_datarow, rq1id_exist, is_rq1id_duplicated


# TEST COMMENT

def create_master_data():
    """create master data from prime and rq1 data"""

    prime_file_exist = os.path.isfile(PRIME_FILE_PATH)
    rqone_file_exist = os.path.isfile(RQONE_FILE_PATH)

    if prime_file_exist and rqone_file_exist:

        # load data from file paths
        prime_data = pd.read_excel(PRIME_FILE_PATH)
        rqone_data = pd.read_excel(RQONE_FILE_PATH)

        cleaned_prime_data_df = clean_prime_data(prime_data)

        # initialize empty list
        master_data_list = []

        for _, row in rqone_data.iterrows():
            # print("=="*20)
            rqone_datarow = list(unzip_rqone_datarow(row))
            rqoneid = str(rqone_datarow[0])

            rq1d_exist_in_prime = rq1id_exist(cleaned_prime_data_df, rqoneid)

            prime_total_work = "-"
            prime_actual_work = "-"
            prime_remain_work = "-"

            if rq1d_exist_in_prime:

                rq1id_duplicated_in_prime = is_rq1id_duplicated(cleaned_prime_data_df, rqoneid)

                # print("[DEBUG]:", rq1id_duplicated_in_prime,
                # "\n", cleaned_prime_data_df.loc[rqoneid])

                if rq1id_duplicated_in_prime:
                    prime_total_work = cleaned_prime_data_df.loc[rqoneid].iloc[-1]["TotalWork"]
                    prime_actual_work = cleaned_prime_data_df.loc[rqoneid].iloc[-1]["ActualWork"]
                    prime_remain_work = cleaned_prime_data_df.loc[rqoneid].iloc[-1]["RemainWork"]

                else:
                    prime_total_work = cleaned_prime_data_df.loc[rqoneid]["TotalWork"]
                    prime_actual_work = cleaned_prime_data_df.loc[rqoneid]["ActualWork"]
                    prime_remain_work = cleaned_prime_data_df.loc[rqoneid]["RemainWork"]

                # print("[DEBUG]:effort:", prime_total_work, prime_actual_work, prime_remain_work)

            # finally:
            rqone_datarow.extend([prime_total_work, prime_actual_work, prime_remain_work])
            master_data_list.append(rqone_datarow)

    return master_data_list


master_data = create_master_data()
master_data_df = pd.DataFrame(master_data,
                              columns=["ID",
                                       "Title",
                                       "LifeCycleState",
                                       "Submitter",
                                       "SubmitDate",
                                       "AccountNumbers",
                                       "EstimatedEffort",
                                       "Allocation",
                                       "Category",
                                       "assignee",
                                       "TotalWork",
                                       "ActualWork",
                                       "RemainWork"])

master_data_df.to_csv("./_out/master_data.csv")
