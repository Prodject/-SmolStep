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
        col_names = [
            "UID",
            "Email",
            "Password",
            "Position",
            "Cert",
        ]
        # Выполняем загрузку данных из dataframe
        try:
            # Выполняем поиск данных в dataframe
            # with open(PD_DB, "rb") as f:
            #     df = pd.read_msgpack(f.read())
            df = pq.read_table(PD_DB, columns=col_names).to_pandas()
            # print(df)

            # Если уже существуют данные
            try:
                # Получаем позицию строки (index)
                df_new = df[(df["UID"] == login) & (df["Password"] == password)]
                print(df_new["Cert"].values[0])
                load_cert = df_new["Cert"].values[0]
                # print(load_cert)
                return load_cert
            except:
                return False
        except:
            return False
