import sys
from typing import Dict 
import dill
import pickle
import numpy as np
from zipfile import Path

class MainUtils: 

    @staticmethod
    def dump_pickle_file(output_filepath: str, data) -> None:
        try:
            with open(output_filepath, "wb") as encoded_pickle:
                pickle.dump(data, encoded_pickle)
        except Exception as e:
            raise NerException(e, sys) from e
    

    @staticmethod
    def load_pickle_file(filepath: str) -> object:
        try:
            with open(filepath, "rb") as pickle_obj:
                obj = pickle.load(pickle_obj)
            return obj
        except Exception as e:
            raise NerException(e, sys) from e