from flet import *
from pages.auth import Auth
from pages.home import Home
from pages.dashboard import Dashboard
from utils.config import SERVER_PORT
import os

# from pages.authority import Authority

APP_PATH = ""
# APP_PORT = 8500


class Main(UserControl):
    def __init__(
        self,
        page: Page,
    ):
        super().__init__
        self.page = page
        self.page.window_height = 780
        self.page.window_width = 850
        self.init_helper()

    def init_helper(
        self,
    ):
        self.page.on_route_change = self.on_route_change
        self.page.go("/")

    def on_route_change(self, route):
        new_page = {
            # "/": Auth,
            "/": Auth,
            # "/": Dashboard,
            # "/authority": Authority,
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(View(route, [new_page]))


# if __name__ == "__main__":
#     flet_path = os.getenv("FLET_PATH", APP_PATH)
#     flet_port = int(os.getenv("FLET_PORT", APP_PORT))
#     app(name=flet_path, assets_dir='assets', view=WEB_BROWSER, target=Main, port=flet_port)
app(
    target=Main,
    assets_dir="assets",
    upload_dir="uploads",
    port=SERVER_PORT,
    view=WEB_BROWSER,
)
