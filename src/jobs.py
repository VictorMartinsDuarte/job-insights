from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as csv_data:
        dict_data = csv.DictReader(csv_data, delimiter=',')
        list_data = list(dict_data)
        return list_data
    # Ref: https://linuxhint.com/import-csv-to-list-python/
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
