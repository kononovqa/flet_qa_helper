import urllib3
import os
import uvicorn
import flet_fastapi
import flet as ft

from router import Router

from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi_client.apis import api

from components.container.container import Containers
from components.progress_bar.progress_bar import ProgressBars
from components.text.text import Texts


async def main(page: ft.Page):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    page.title = "Flet QA Helper"
    page.horizontal_alignment = "center"
    page.theme_mode = "dark"
    page.scroll = 'AUTO'

    myRouter = Router(page)
    page.on_route_change = myRouter.route_change
    await page.add_async(myRouter.body)
    await page.go_async('/')

    async def go_start(e):
        await page.go_async('/')

    async def go_tools(e):
        await page.go_async('/tools')

    async def go_info(e):
        await page.go_async('/info')

    async def go_autotests(e):
        await page.go_async('/autotests')

    async def go_stands(e):
        await page.go_async('/stands')

    button_create = ft.TextButton(
        content=Texts().txt_header_main(),
        on_click=go_start)

    button_helper = ft.TextButton(
        content=Texts().txt_header_tools(),
        on_click=go_tools)

    button_info = ft.TextButton(
        content=Texts().txt_header_info(),
        on_click=go_info)

    button_autotests = ft.TextButton(
        content=Texts().txt_header_autotests(),
        on_click=go_autotests)

    button_stands = ft.TextButton(
        content=Texts().txt_header_stands(),
        on_click=go_stands)

    page.appbar = ft.AppBar(
        title=ft.Column([
            ft.Row(
                [button_create, ProgressBars().vertical_divider, button_helper,
                 ProgressBars().vertical_divider, button_autotests,
                 ProgressBars().vertical_divider, button_stands,
                 ProgressBars().vertical_divider, button_info],
                alignment=ft.MainAxisAlignment.CENTER,
                offset=(0, 0.4)),
            ft.Row(
                [Containers().horizontal_divider],
                height=16,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.alignment.bottom_center,
                offset=(0, 1))
        ]),
        toolbar_height=75)

    await page.update_async()


def custom_openapi():
    openapi_schema = get_openapi(
        title="Упс, сваггер не тут",
        version="3.1.0",
        summary="",
        description=f"Документация располагается на [host/api/docs](host/api/docs)",
        routes=[],
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = flet_fastapi.FastAPI()
app.openapi = custom_openapi


app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/api", app=api)
app.mount("/", flet_fastapi.app(main,
                                assets_dir=os.getcwd() + '/assets',
                                web_renderer=ft.WebRenderer.CANVAS_KIT.AUTO))

if __name__ == "__main__":
    uvicorn.run("start:app", log_level="info")
