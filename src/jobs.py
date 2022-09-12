from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as csv_data:
        dictData = csv.DictReader(csv_data, delimiter=',')
        listData = list(dictData)
        return listData
    # """Reads a file from a given path and returns its contents

    # Parameters
    # ----------
    # path : str
    #     Full path to file

    # Returns
    # -------
    # list
    #     List of rows as dicts
    # """
