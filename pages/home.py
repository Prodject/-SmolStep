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
                ResponsiveRow(
                    alignment=MainAxisAlignment.CENTER,
                    # spacing = 2,
                    # columns = 2,
                    controls=[
                        Column(
                            col={"xs": 12, "sm": 12},
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                Container(
                                    width=700,
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
                                                                "Правила использования сервиса",
                                                                size=16,
                                                                weight="bold",
                                                            ),
                                                        ],
                                                    ),
                                                    Divider(
                                                        height=10, color="transparent"
                                                    ),
                                                    # Добавление текстового поля
                                                    Column(
                                                        width=650,
                                                        height=450,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        # Добавление прокрутки
                                                        expand=True,
                                                        scroll="hidden",
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        controls=[
                                                            Text(
                                                                "Proin rutrum, purus sit amet elementum volutpat, nunc lacus vulputate orci, cursus ultrices neque dui quis purus. Ut ultricies purus nec nibh bibendum, eget vestibulum metus varius. Duis convallis maximus justo, eu rutrum libero maximus id. Donec ullamcorper arcu in sapien molestie, non pellentesque tellus pellentesque. Nulla nec tristique ex. Maecenas euismod nisl enim, a convallis arcu laoreet at. Ut at tortor finibus, rutrum massa sit amet, pulvinar velit. Phasellus diam lorem, viverra vitae leo vitae, consequat suscipit lorem.",
                                                            ),
                                                            Text(
                                                                "Proin rutrum, purus sit amet elementum volutpat, nunc lacus vulputate orci, cursus ultrices neque dui quis purus. Ut ultricies purus nec nibh bibendum, eget vestibulum metus varius. Duis convallis maximus justo, eu rutrum libero maximus id. Donec ullamcorper arcu in sapien molestie, non pellentesque tellus pellentesque. Nulla nec tristique ex. Maecenas euismod nisl enim, a convallis arcu laoreet at. Ut at tortor finibus, rutrum massa sit amet, pulvinar velit. Phasellus diam lorem, viverra vitae leo vitae, consequat suscipit lorem.",
                                                            ),
                                                            Text(
                                                                "Proin rutrum, purus sit amet elementum volutpat, nunc lacus vulputate orci, cursus ultrices neque dui quis purus. Ut ultricies purus nec nibh bibendum, eget vestibulum metus varius. Duis convallis maximus justo, eu rutrum libero maximus id. Donec ullamcorper arcu in sapien molestie, non pellentesque tellus pellentesque. Nulla nec tristique ex. Maecenas euismod nisl enim, a convallis arcu laoreet at. Ut at tortor finibus, rutrum massa sit amet, pulvinar velit. Phasellus diam lorem, viverra vitae leo vitae, consequat suscipit lorem.",
                                                            ),
                                                            Text(
                                                                "Proin rutrum, purus sit amet elementum volutpat, nunc lacus vulputate orci, cursus ultrices neque dui quis purus. Ut ultricies purus nec nibh bibendum, eget vestibulum metus varius. Duis convallis maximus justo, eu rutrum libero maximus id. Donec ullamcorper arcu in sapien molestie, non pellentesque tellus pellentesque. Nulla nec tristique ex. Maecenas euismod nisl enim, a convallis arcu laoreet at. Ut at tortor finibus, rutrum massa sit amet, pulvinar velit. Phasellus diam lorem, viverra vitae leo vitae, consequat suscipit lorem.",
                                                            ),
                                                            Text(
                                                                "Proin rutrum, purus sit amet elementum volutpat, nunc lacus vulputate orci, cursus ultrices neque dui quis purus. Ut ultricies purus nec nibh bibendum, eget vestibulum metus varius. Duis convallis maximus justo, eu rutrum libero maximus id. Donec ullamcorper arcu in sapien molestie, non pellentesque tellus pellentesque. Nulla nec tristique ex. Maecenas euismod nisl enim, a convallis arcu laoreet at. Ut at tortor finibus, rutrum massa sit amet, pulvinar velit. Phasellus diam lorem, viverra vitae leo vitae, consequat suscipit lorem.",
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
