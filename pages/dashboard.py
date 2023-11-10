import flet
from flet import *
import time
import datetime
import shutil
import glob
import os
import re
import random
from math import pi
from typing import Dict
from utils.colors import *
from utils.gradient_colors import *
from utils.navbar import NavBar, PostBar
from utils.validation import Validator
from utils.config import (
    SERVER_URL,
    SERVER_PORT,
    SUBNET_NET,
    GATEWAY,
    # SERVICE_STATUS,
    # SERVICE_NOTIFICATION,
    # SERVICE_DATE,
)

# Добавление управляющих элементов на страницу входа


class Dashboard(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        # self.bgcolor = 'blue'
        # Убирает рамку
        # self.margin = -10
        self.offset = transform.Offset(
            0,
            0,
        )
        self.alignment = alignment.center
        self.ztheme = "light"
        # Инициализация валидатора
        self.validator = Validator()
        # Первичный текст баннера
        self.WarningText = "Произошла ошибка"
        # Инициализация ошибочного окраса полей
        self.error_border = border.all(width=1, color="red")
        # page.bgcolor = '#1f262f'
        # page.bgcolor = colors.DEEP_PURPLE_300
        self.ip_checked = []
        self.all_ips = []
        self.seconds = ""

        # Функция смены темы
        def change_theme(e):
            if self.ztheme == "light":
                self.bgcolor = ("#1f262f",)
                self.ztheme = "dark"
            else:
                self.bgcolor = "blue"
                self.ztheme = "light"
            page.update()
