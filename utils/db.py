# import lib
import os
from pathlib import Path
import pandas as pd
from utils.config import PD_DB
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq


class PDDB:
    def __init__(self):
        pass

    # Функция сохранения данных в pandas через pickle / msgpack
    def save(self, ip, mac, select):
        col_names = [
            "IP",
            "MAC",
            "SELECT",
        ]
        values = [ip, mac, select]

        try:
            # Выполняем поиск данных в dataframe
            # with open(PD_DB, "rb") as f:
            #     df = pd.read_msgpack(f.read())
            df = pq.read_table(PD_DB, columns=col_names).to_pandas()
            print(df)

            # Формируем датафрейм
            df.loc[len(df.index)] = values
            table = pa.Table.from_pandas(df)
            # Выполняем сохранение
            pq.write_table(table, PD_DB)

        # Если нет данных совсем
        except:
            df = pd.DataFrame([values], columns=col_names)
            table = pa.Table.from_pandas(df)
            # pq.write_table(table, "example.parquet")
            # df.to_pa

            # Выполняем сохранение
            pq.write_table(table, PD_DB)

        return True

    # Функция обновления данных в pandas через pickle / msgpack
    def update(self, ip, mac, select):
        col_names = [
            "IP",
            "MAC",
            "SELECT",
        ]
        values = [ip, mac, select]

        try:
            # Выполняем поиск данных в dataframe
            # with open(PD_DB, "rb") as f:
            #     df = pd.read_msgpack(f.read())
            df = pq.read_table(PD_DB, columns=col_names).to_pandas()
            print(df)

            # Если уже существуют данные
            try:
                # Если требуется заменить данные, пароль например

                # Получаем позицию строки (index)
                df_new = df[(df["IP"] == ip) & (df["MAC"] == mac)].index[0]
                print(df_new)
                # Заменяем значения в dataframe (оригинальном)
                # df.at[df_new, "IP"] = ip
                # df.at[df_new, "MAC"] = mac
                # df.at[df_new, "Password"] = password
                df.at[df_new, "SELECT"] = select

                # df_new.loc[0] = [email, password, position, cert]
                # print(df_new)
                # df = df.appen(df_new)
                table = pa.Table.from_pandas(df)
                # Выполняем сохранение
                pq.write_table(table, PD_DB)

            # Если совпадений нет
            except:
                # Формируем датафрейм
                df.loc[len(df.index)] = values
                table = pa.Table.from_pandas(df)
                # Выполняем сохранение
                pq.write_table(table, PD_DB)

        # Если нет данных совсем
        except:
            df = pd.DataFrame([values], columns=col_names)
            table = pa.Table.from_pandas(df)
            # pq.write_table(table, "example.parquet")
            # df.to_pa

            # Выполняем сохранение
            pq.write_table(table, PD_DB)

        return True
