import flet
from flet import *
import random
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


class Home(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.scroll = "Adaptive"
        # self.bgcolor = 'blue'
        # Убирает рамку
        # self.margin = -10
        self.offset = transform.Offset(
            0,
            0,
        )
        self.alignment = alignment.center
        self.ztheme = "light"
        # page.bgcolor = '#1f262f'
        # page.bgcolor = colors.DEEP_PURPLE_300

        # Функция смены темы
        def change_theme(e):
            if self.ztheme == "light":
                self.bgcolor = ("#1f262f",)
                self.ztheme = "dark"
            else:
                self.bgcolor = "blue"
                self.ztheme = "light"
            page.update()

        random_test_backgroud = random.randint(0, len(backgroud_color_list) - 1)

        panels = Column(
            # scroll="adaptive",
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
                # _title_navbar,
                Divider(height=30, color="transparent"),
                # Container(
                #     content=Text("Hello"),
                #     image_src="https://picsum.photos/100/100",
                #     width=100,
                #     height=100,
                # ),
                # Row(alignment=MainAxisAlignment.CENTER, controls=[])
                # Stack(
                #     controls=[
                #         Container(
                #             height=1000,
                #             width=1000,
                #             left=60,
                #             top=-200,
                #             content=Image(
                #                 src="assets/background/2.jpg",
                #                 scale=0.9,
                #                 fit=ImageFit.CONTAIN,
                #             ),
                #         )
                #     ]
                # ),
                ResponsiveRow(
                    alignment=MainAxisAlignment.CENTER,
                    # spacing = 2,
                    # columns = 2,
                    controls=[
                        Column(
                            col={
                                "xs": 12,
                                "sm": 12,
                                "md": 6,
                                "lg": 6,
                                "xl": 4,
                                "xxl": 4,
                            },
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                Container(
                                    width=700,
                                    height=630,
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
                                                    Stack(controls=[]),
                                                    # Add text
                                                    Divider(
                                                        height=5, color="transparent"
                                                    ),
                                                    Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        spacing=5,
                                                        controls=[
                                                            Text(
                                                                "Смоленск по шагам",
                                                                size=50,
                                                                weight=FontWeight.W_100,
                                                            ),
                                                            Text(
                                                                "Смоленск - город с богатой  историей и культурой, но мы предлагаем Вам посмотреть на него по-новому. Постройте маршрут и прогуляйтесь по туристическим местам и малознакомым уголкам древнего города",
                                                                size=16,
                                                                weight="bold",
                                                                text_align="JUSTIFY",
                                                            ),
                                                        ],
                                                    ),
                                                    Divider(
                                                        height=2, color="transparent"
                                                    ),
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        # controls=[
                                                        #     self.change_passwd,
                                                        # ],
                                                    ),
                                                    # Добавление поля ввода ФИО
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        # controls=[
                                                        #     self.client_name,
                                                        # ],
                                                    ),
                                                    # Добавление поля ввода организации
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        # controls=[
                                                        #     self.client_org,
                                                        # ],
                                                    ),
                                                    # Добавление поля ввода должности
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        # controls=[
                                                        #     self.client_position,
                                                        # ],
                                                    ),
                                                    # Добавление поля ввода почты
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        # controls=[
                                                        #     self.client_email,
                                                        # ],
                                                    ),
                                                    # Вывод поля уникального номера сертификата
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        # controls=[
                                                        #     self.client_cert_key,
                                                        # ],
                                                    ),
                                                    # Добавление поля действительности сертификата
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        # controls=[
                                                        #     self.client_valid,
                                                        # ],
                                                    ),
                                                    # Колонка вывода последних файлов
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                    ),
                                                ],
                                            ),
                                        )
                                    ),
                                )
                            ],
                        ),
                        Column(
                            col={
                                "xs": 12,
                                "sm": 12,
                                "md": 6,
                                "lg": 6,
                                "xl": 4,
                                "xxl": 4,
                            },
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                Container(
                                    width=400,
                                    height=630,
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
                                                    Stack(controls=[]),
                                                    # Add text
                                                    Divider(
                                                        height=5, color="transparent"
                                                    ),
                                                    Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        spacing=5,
                                                        controls=[
                                                            Text(
                                                                "Подпись документов",
                                                                size=16,
                                                                weight="bold",
                                                            ),
                                                        ],
                                                    ),
                                                    Divider(
                                                        height=40, color="transparent"
                                                    ),
                                                    # Добавление поля отметки документа
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        # controls=[
                                                        #     self.reject_message,
                                                        # ],
                                                    ),
                                                    # Добавление кнопок
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        # controls=[
                                                        #     self.external_signature,
                                                        #     self.finalized,
                                                        #     self.email_send,
                                                        # ],
                                                    ),
                                                    Column(
                                                        width=350,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        controls=[
                                                            PopupMenuButton(
                                                                icon=icons.CLOUD_DOWNLOAD_OUTLINED,
                                                                items=[
                                                                    PopupMenuItem(
                                                                        text="Подписать",
                                                                        # on_click=sign_use,
                                                                    ),
                                                                    PopupMenuItem(
                                                                        text="Согласовать",
                                                                        # on_click=sign_approve,
                                                                    ),
                                                                    PopupMenuItem(
                                                                        text="Утвердить",
                                                                        # on_click=sign_coniform,
                                                                    ),
                                                                    PopupMenuItem(
                                                                        text="Отклонить",
                                                                        # on_click=sign_reject,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Divider(
                                                        height=20, color="transparent"
                                                    ),
                                                    # Добавление кнопки выбора файла
                                                    ElevatedButton(
                                                        "Выбрать файл для подписи (pdf)",
                                                        icon=icons.ATTACH_FILE,
                                                        # on_click=lambda _: file_picker.pick_files(
                                                        #     allow_multiple=False,
                                                        #     file_type="pdf",
                                                        # ),
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
                                                            bgcolor={
                                                                "": colors.PINK_300
                                                            },
                                                        ),
                                                        height=40,
                                                        width=300,
                                                    ),
                                                    # Колонка вывода выбираемого сертификата
                                                    # Column(ref=files),
                                                    Divider(
                                                        height=2, color="transparent"
                                                    ),
                                                    # Добавление кнопки подписать документ
                                                    ElevatedButton(
                                                        "Подписать документ",
                                                        # ref=upload_button,
                                                        icon=icons.ASSIGNMENT_RETURNED_ROUNDED,
                                                        # on_click=sign,
                                                        # on_click=presign,
                                                        # ref=upload_button,
                                                        # on_click=upload_files,
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
                                                            bgcolor={
                                                                "": colors.CYAN_400
                                                            },
                                                        ),
                                                        height=40,
                                                        width=300,
                                                    ),
                                                    Divider(
                                                        height=2, color="transparent"
                                                    ),
                                                    # Добавление кнопки отправки на почту
                                                    ElevatedButton(
                                                        "Отправить на почту",
                                                        # ref=upload_button,
                                                        icon=icons.EMAIL,
                                                        # on_click=upload_files,
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
                                                            bgcolor={
                                                                "": colors.YELLOW_600
                                                            },
                                                        ),
                                                        height=40,
                                                        width=300,
                                                    ),
                                                ],
                                            ),
                                        )
                                    ),
                                )
                            ],
                        ),
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

        self.content = Container(
            expand=True,
            width=10000,
            # height = page.height,
            margin=-10,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.bottom_right,
                colors=backgroud_color_list[random_test_backgroud],
            ),
            content=panels,
        )
