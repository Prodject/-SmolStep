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
                                    height=500,
                                    content=Container(
                                        border_radius=6,
                                        content=Column(
                                            # horizontal_alignment=CrossAxisAlignment.CENTER,
                                            # alignment = MainAxisAlignment.CENTER,
                                            # Добавляение управляющих элементов
                                            controls=[
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
                                            ],
                                        ),
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
                                    width=900,
                                    height=500,
                                    content=Container(
                                        border_radius=6,
                                        content=Column(
                                            # horizontal_alignment=CrossAxisAlignment.CENTER,
                                            # alignment = MainAxisAlignment.CENTER,
                                            # Добавляение управляющих элементов
                                            controls=[
                                                Column(
                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                                    spacing=5,
                                                    controls=[
                                                        Image(
                                                            src="assets/background/2.jpg",
                                                            scale=0.9,
                                                            fit=ImageFit.CONTAIN,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                )
                            ],
                        ),
                        #
                    ],
                ),
                # Column(
                #     horizontal_alignment=CrossAxisAlignment.CENTER,
                #     controls=[
                #         Divider(height=5, color="transparent"),
                #         Column(
                #             alignment=MainAxisAlignment.CENTER,
                #             horizontal_alignment=CrossAxisAlignment.CENTER,
                #             spacing=5,
                #             controls=[
                #                 Text(
                #                     "Информация о сертификате",
                #                     size=16,
                #                     weight="bold",
                #                 ),
                #             ],
                #         ),
                #     ],
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
                                    content=Container(
                                        border_radius=6,
                                        content=Column(
                                            # horizontal_alignment=CrossAxisAlignment.CENTER,
                                            # alignment = MainAxisAlignment.CENTER,
                                            # Добавляение управляющих элементов
                                            controls=[
                                                Column(
                                                    alignment=MainAxisAlignment.CENTER,
                                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                                    spacing=5,
                                                    controls=[
                                                        Text(
                                                            "Приглашаем прогуляться по старинному городу Смоленску, используя нашу платформу. Мы создали маршруты, выбирая самые красивые, зрелищные и интересные места. Маршруты могут пролегать как в городе, так и за его пределами, иметь разную сложность и продолжительность. Маршруты адаптированы под самые разные категории людей. Они будут интересны как туристам, так и жителям города. Путешествуя с нами, вы узнаете много нового и интересного, познакомитесь с историческими местами, живописными парками, а также сможете полюбоваться Смоленском со смотровых площадок. Чтобы больше узнать о городе, его секретах и интересных фактах, мы подготовили аудиогид. С ним прогулки станут еще интереснее и увлекательнее!",
                                                            size=16,
                                                            weight="bold",
                                                            text_align="JUSTIFY",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
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
