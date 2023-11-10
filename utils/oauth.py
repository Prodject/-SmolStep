# import lib
import os
from pathlib import Path

# import pandas as pd
from utils.config import PD_DB
import hashlib

# import numpy as np
# import pyarrow as pa
# import pyarrow.parquet as pq


class oauth:
    def __init__(self):
        pass

    # Функция валидации заполненности полей
    def auth_validate(self, login, password):
        if(login != "" and password != ""):
            print("auth_validated")
            return True
        else:
            print("auth_INVALIDATED")
            return False