import os
import sys 
sys.path.insert(0, 'G:/ml_project_01/')
sys.path.insert(0, 'G:/ml_project_01/src/')
import numpy as np
import pandas as pd
import dill

from src.exception import CostumException
 
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CostumException(e, sys)