from flet import *


class NavBar(UserControl):
    def __init__(
        self,
        name_home,
        url_home,
        name_route,
        url_route,
        name_news,
        url_news,
        name_report,
        url_report,
        name_contact,
        url_contact,
    ):
        #         self.name_home = "Главная"
        #         self.url_home = lambda _: self.page.go("/")
        #         self.name_route = "Маршрут"
        #         self.url_route = lambda _: self.page.go("/route")
        #         self.name_news = "Новости"
        #         self.url_news = lambda _: self.page.go("/news")
        #         self.name_report = "Отзывы"
        #         self.url_report = lambda _: self.page.go("/report")
        #         self.name_contact = "Контакты"
        #         self.url_contact = lambda _: self.page.go("/contact")
        self.name_home = name_home
        self.url_home = url_home
        self.name_route = name_route
        self.url_route = url_route
        self.name_news = name_news
        self.url_news = url_news
        self.name_report = name_report
        self.url_report = url_report
        self.name_contact = name_contact
        self.url_contact = url_contact
        super().__init__()

    def build(self):
        return Container(
            # Добавление прокрутки
            bgcolor=colors.BLACK,
            content=Row(
                alignment="end",
                controls=[
                    Container(
                        padding=padding.only(right=20),
                        height=64,
                        content=Row(
                            controls=[
                                Text(
                                    size=16,
                                    spans=[
                                        TextSpan(
                                            self.name_home,
                                            # weight = 'w600',
                                            # url = self.url_home,
                                            on_click=self.url_home,
                                            # on_enter=highlight_link,
                                            # on_exit=unhighlight_link,
                                            # name = link_usage,
                                        ),
                                        TextSpan("  "),
                                        TextSpan(
                                            self.name_route,
                                            # weight = 'w600',
                                            # url = self.url_usage,
                                            on_click=self.url_route
                                            # on_enter=highlight_link,
                                            # on_exit=unhighlight_link,
                                        ),
                                        TextSpan("  "),
                                        TextSpan(
                                            self.name_news,
                                            # weight = 'w600',
                                            url=self.url_news,
                                            # on_enter=highlight_link,
                                            # on_exit=unhighlight_link,
                                        ),
                                        TextSpan("  "),
                                        TextSpan(
                                            self.name_report,
                                            # weight = 'w600',
                                            url=self.url_report,
                                            # on_enter=highlight_link,
                                            # on_exit=unhighlight_link,
                                        ),
                                        TextSpan("  "),
                                        TextSpan(
                                            self.name_contact,
                                            # weight = 'w600',
                                            url=self.url_contact,
                                            # on_enter=highlight_link,
                                            # on_exit=unhighlight_link,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )


class PostBar(UserControl):
    def __init__(
        self, name_link_support, url_link_support, name_link_about, url_link_about
    ):
        self.name_link_support = name_link_support
        self.url_link_support = url_link_support
        self.name_link_about = name_link_about
        self.url_link_about = url_link_about
        super().__init__()

    def build(self):
        return Container(
            # bgcolor=colors.BLACK,
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        # width = 300,
                        # height = 100,
                        content=Row(
                            controls=[
                                Text(
                                    size=16,
                                    spans=[
                                        TextSpan(
                                            # self.public_token,
                                            "Активный токен: 94S****35FF",
                                            # weight = 'w600',
                                            # url = self.url_home,
                                            # on_enter=highlight_link,
                                            # on_exit=unhighlight_link,
                                            # name = link_usage,
                                        ),
                                        TextSpan(" | "),
                                    ],
                                ),
                                Divider(height=5, color="transparent"),
                                IconButton(
                                    icon_color="white",
                                    # opacity = 0,
                                    icon=icons.CONTACT_SUPPORT,
                                    # icon_color="blue400",
                                    icon_size=20,
                                    tooltip="Обратная связь",
                                ),
                                IconButton(
                                    icon_color="white",
                                    icon=icons.DEVELOPER_MODE,
                                    # icon_color="blue400",
                                    icon_size=20,
                                    tooltip="Лаборатория информатизации",
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )


_title_navbar = ResponsiveRow(
    alignment="center",
    controls=[
        Container(
            col={"xs": 12, "sm": 8, "md": 10, "lg": 10, "xl": 12},
            alignment=alignment.top_center,
            padding=20,
            content=Text(
                "Электронный документооборот",
                size=45,
                weight="w600",
                text_align="center",
            ),
        ),
        # Divider(height=30, color = 'transparent'),
    ],
)


# class NavBar(UserControl):
#     def __init__(self):
#         self.name_home = "Главная"
#         self.url_home = lambda _: self.page.go("/")
#         self.name_route = "Маршрут"
#         self.url_route = lambda _: self.page.go("/route")
#         self.name_news = "Новости"
#         self.url_news = lambda _: self.page.go("/news")
#         self.name_report = "Отзывы"
#         self.url_report = lambda _: self.page.go("/report")
#         self.name_contact = "Контакты"
#         self.url_contact = lambda _: self.page.go("/contact")
#         # old
#         self.name_external = "OPNSense"
#         self.url_external = "https://37.44.46.51:444"
#         super().__init__()
