import flet
from flet import *
import time
from math import pi
from typing import Dict
from utils.oauth import *
from utils.colors import *
from utils.gradient_colors import *
from utils.navbar import NavBar, PostBar
from utils.config import *
from utils.validation import *
from service.session import *
import shutil
import datetime

# Добавление управляющих элементов на страницу входа


class Auth(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = "blue"
        # Убирает рамку
        self.margin = -10
        self.offset = transform.Offset(
            0,
            0,
        )
        self.alignment = alignment.center
        self.ztheme = "light"

        # Первичный текст баннера
        self.WarningText = "Ошибка авторизации"
        # page.bgcolor = '#1f262f'
        # page.bgcolor = colors.DEEP_PURPLE_300

        # Проверка уведомлений
        try:
            self.noti_status = page.session.get("setting_notification_status")
            self.noti_label = page.session.get("setting_notification_label")
        except:
            self.noti_status = False
            self.noti_label = "Планируется проведение работ 01.01.01 01:01"

        # Функция смены темы
        def change_theme(e):
            if self.ztheme == "light":
                self.bgcolor = ("#1f262f",)
                self.ztheme = "dark"
            else:
                self.bgcolor = "blue"
                self.ztheme = "light"
            page.update()

        def WarningClose(e):
            self.banners.open = False
            page.update()

        def BannerWorkClose(e):
            self.banner_work.open = False
            page.update()

        # Инициализация окна баннера
        self.banner_element = Ref[Column]()

        # Инициализация окна баннера
        self.banner_tech = Ref[Column]()

        # Инициализация элемента кнопки токена
        login_input = Ref[Column]()
        password_input = Ref[Column]()
        self.token_init = 0
        self.password_init = 0
        upload_button = Ref[ElevatedButton]()

        # Поле токена

        self.login_field = TextField(
            label="Логин", border="none", text_size=14, text_align="center"
        )

        self.password_field = TextField(
            label="Пароль", border="none", text_size=14, text_align="center"
        )


        def store_session(file_session):
            # Получаем из сертификата наименование папки

            # Копируем сертификат пользователя в папку сессии
            # os.mkdir(r"service/sessions/" + file_session)
            shutil.copy2("uploads/" + file_session, r"service/sessions/" + file_session)
            # Сохраняем значение ключа в глобальную перменную
            page.session.set("session", r"service/sessions/" + file_session)

        def auth(e):
            print("LOL")

            print("auth(e) started")
            # Если введен логин и пароль и не введен токен
            if self.login_field.value != "" and self.password_field.value != "":
                print("self.login and self.pass passed")
                # Выполняем проверку логина и пароля
                auth_cert = oauth.auth_validate(
                    self, self.login_field.value, self.password_field.value
                )
                print("auth_cert passed")
                print(auth_cert)
                if auth_cert != False:
                    # Выполняем загрузку сертификата
                    # Сохраняем данные в сессию авторизации
                    page.session.set("session", auth_cert)
                    print('test')
                    self.page.go("/")
                    return page.update()
                else:
                    self.content.update()
                    self.banner_element.current.controls.append(
                        Row(controls=[self.banners], alignment="center")
                    )
                    self.banners.open = True
                    page.update()

        self.banners = Banner(
            bgcolor=colors.AMBER_300,
            leading=Icon(icons.WARNING_AMBER_ROUNDED, color=colors.AMBER, size=40),
            content=Text(self.WarningText, color=colors.BLACK),
            actions=[
                FilledButton("Закрыть", on_click=WarningClose),
            ],
        )

        self.banner_work = Banner(
            bgcolor=colors.AMBER_300,
            leading=Icon(icons.WARNING_AMBER_ROUNDED, color=colors.AMBER, size=40),
            content=Text(self.noti_label, color=colors.BLACK),
            actions=[
                FilledButton("Закрыть", on_click=BannerWorkClose),
            ],
        )

        self.content = Column(
            # Добавление прокрутки
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Stack(
                    controls=[
                        NavBar(
                            "Главная",
                            lambda _: self.page.go("/"),
                            "Маршрут",
                            lambda _: self.page.go("/route"),
                            "Новости",
                            lambda _: self.page.go("/news"),
                            "Отзывы",
                            lambda _: self.page.go("/report"),
                            "Контакты",
                            lambda _: self.page.go("/contact"),
                        )
                    ],
                ),
                # Добавление строки баннера технических работ
                Column(ref=self.banner_tech),
                # Добавление строки баннера
                Column(ref=self.banner_element),
                # _title_navbar,
                Divider(height=30, color="transparent"),
                Column(
                    expand=True,
                    scroll="hidden",
                    controls=[
                        Container(
                            width=408,
                            height=500,
                            content=Card(
                                content=Container(
                                    # shadow=BoxShadow(
                                    #     spread_radius=1,
                                    #     blur_radius=24,
                                    #     color=colors.BLUE,
                                    #     offset=Offset(0, 0),
                                    #     blur_style=ShadowBlurStyle.OUTER,
                                    # ),
                                    # bgcolor = 'white',
                                    # bgcolor=colors.GREY_900,
                                    # bgcolor = '#23262a',
                                    # gradient = LinearGradient(
                                    #      begin = alignment.bottom_left,
                                    #      end = alignment.top_right,
                                    #      colors = ['#13547a', '#80dc7'],
                                    # ),
                                    border_radius=6,
                                    content=Column(
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        # alignment = MainAxisAlignment.CENTER,
                                        # Добавляение управляющих элементов
                                        controls=[
                                            Divider(height=10, color="transparent"),
                                            Stack(controls=[]),
                                            # Add text
                                            Divider(height=30, color="transparent"),
                                            Column(
                                                alignment=MainAxisAlignment.CENTER,
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                spacing=5,
                                                controls=[
                                                    Text(
                                                        "Смоленск по шагам",
                                                        size=22,
                                                        weight="bold",
                                                    ),
                                                    Text(
                                                        "Вход в систему",
                                                        size=13,
                                                        weight="bold",
                                                    ),
                                                ],
                                            ),
                                            # Добавление поля ввода логина
                                            Column(
                                                width=350,
                                                alignment=MainAxisAlignment.CENTER,
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                controls=[
                                                    self.login_field,
                                                ],
                                            ),
                                            # Добавление поля ввода пароля
                                            Column(
                                                width=350,
                                                alignment=MainAxisAlignment.CENTER,
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                controls=[
                                                    self.password_field,
                                                ],
                                            ),
                                            Divider(height=30, color="transparent"),
                                            # Добавление кнопки авторизации
                                            ElevatedButton(
                                                "Авторизация",
                                                ref=upload_button,
                                                icon=icons.VERIFIED_USER_OUTLINED,
                                                # on_click=print("clicked"),
                                                on_click=auth,
                                                # on_click=self.login,
                                                # on_click=lambda _: page.go('/token'),
                                                disabled=True,
                                                content=Text(
                                                    size=13,
                                                    weight="bold",
                                                ),
                                                style=ButtonStyle(
                                                    shape={
                                                        "": RoundedRectangleBorder(
                                                            radius=13
                                                        ),
                                                    },
                                                    color={
                                                        "": "black",
                                                    },
                                                    bgcolor={"": colors.PINK},
                                                ),
                                                height=40,
                                                width=300,
                                            ),
                                            # Добавление ссылок смены темы
                                            Row(
                                                alignment=MainAxisAlignment.CENTER,
                                                # horizontal_alignment = CrossAxisAlignment.END,
                                                spacing=5,
                                                controls=[
                                                    IconButton(
                                                        icon=icons.COLOR_LENS_OUTLINED,
                                                        on_click=change_theme,
                                                        data=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                )
                            ),
                        )
                    ],
                ),
                Stack(
                    controls=[
                        PostBar(
                            "Главная",
                            "https://esign.sbmpei.ru",
                            "Использование",
                            "https://esign.sbmpei.ru/usage",
                        )
                    ],
                ),
            ],
        )

        # Проверка технических работ
        if self.noti_status == True:
            self.banner_tech.current.controls.append(
                Row(controls=[self.banner_work], alignment="center")
            )
            self.banner_work.open = True
            page.update()
        else:
            self.banner_work.open = False
            page.update()
