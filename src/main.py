"""main application"""

import os
import pandas as pd

from utils.settings import PRIME_FILE_PATH, RQONE_FILE_PATH
from utils.util import get_account_numbers_by_id,\
    clean_prime_data,\
        unzip_prime_datarow,\
            unzip_rqone_datarow,\
                rq1id_exist,\
                    is_rq1id_duplicated,\
                        load_rqone_data


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
        master_data = []

        for _, row in rqone_data.iterrows():
            # id, title, life_cycle_state, submitter, submit_date, \
            #     account_numbers, estimated_effort,\
            #         allocation, category, assignee = unzip_rqone_datarow(row)
            # try:
            rqone_datarow = list(unzip_rqone_datarow(row))
            id = str(rqone_datarow[0])

            rq1d_exist_in_prime = rq1id_exist(cleaned_prime_data_df, id)

            prime_total_work = "-"
            prime_actual_work = "-"
            prime_remain_work = "-"

            if rq1d_exist_in_prime:

                rq1id_duplicated_in_prime = is_rq1id_duplicated(cleaned_prime_data_df, id)

                if rq1id_duplicated_in_prime:
                    prime_total_work = cleaned_prime_data_df.loc[id].iloc[-1]["TotalWork"]
                    prime_actual_work = cleaned_prime_data_df.loc[id].iloc[-1]["ActualWork"]
                    prime_remain_work = cleaned_prime_data_df.loc[id].iloc[-1]["RemainWork"]

                else:
                    prime_total_work = cleaned_prime_data_df.loc[id]["TotalWork"]
                    prime_actual_work = cleaned_prime_data_df.loc[id]["ActualWork"]
                    prime_remain_work = cleaned_prime_data_df.loc[id]["RemainWork"]


            # finally:
            rqone_datarow.extend([prime_total_work, prime_actual_work, prime_remain_work])
            master_data.append(rqone_datarow)

    return master_data


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
        # return id, title, life_cycle_state, submitter, submit_date, account_numbers, \
        #     estimated_effort, estimated_effort, allocation, category, assignee

master_data_df.to_csv("./_out/master_data.csv")
