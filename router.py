import flet as ft

from pages.main_page import main_page
from pages.tools_page import tools_page
from pages.delete_order_page import delete_order_page
from pages.info_page import info_page
from pages.autotests_page import autotests_page
from pages.stands_page import stands_page


class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": main_page(page),
            "/tools": tools_page(page),
            "/tools/delete_order": delete_order_page(page),
            "/info": info_page(page),
            "/autotests": autotests_page(page),
            "/stands": stands_page(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    async def route_change(self, route):
        if route.route == '/autotests':
            self.routes['/autotests'] = autotests_page(self.page)
        self.body.content = self.routes[route.route]
        await self.body.update_async()
