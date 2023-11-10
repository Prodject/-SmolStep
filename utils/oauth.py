# import lib
import os
from pathlib import Path
import sqlite3

# import pandas as pd
from utils.config import PD_DB
import hashlib

# import numpy as np
# import pyarrow as pa
# import pyarrow.parquet as pq


class oauth:
    def auth_validate(self, login, password):
        try:
            # Создаем соединение с базой данных
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            with sqlite3.connect('smolsteps.db') as conn:
                cursor = conn.cursor()

                # Выполняем SQL-запрос
                query = "SELECT * FROM users WHERE login=? AND password=?"
                cursor.execute(query, (login, hashed_password))

                # Получаем результат запроса
                user_data = cursor.fetchone()

                if user_data:
                    # Если пользователь найден, возвращаем True
                    return True
                else:
                    # Если пользователь не найден
                    return False
        except Exception as e:
            print(f"Error: {e}")
            return False
