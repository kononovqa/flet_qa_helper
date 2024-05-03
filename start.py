import urllib3
import os
import uvicorn
import flet_fastapi
import flet as ft

from components.button.elevated_button import ElevatedButtons
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

    async def go_api(e):
        await page.launch_url_async('/api/docs')

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

    button_api = ft.TextButton(
        content=Texts().txt_api_button(),
        on_click=go_api)

    row_header = ft.Row(
        [button_create, ProgressBars().vertical_divider, button_helper,
         ProgressBars().vertical_divider, button_autotests,
         ProgressBars().vertical_divider, button_stands,
         ProgressBars().vertical_divider, button_api,
         ProgressBars().vertical_divider, button_info],
        alignment=ft.MainAxisAlignment.CENTER,
        offset=(0, 0.4))

    horizontal_divider_header = Containers().horizontal_divider
    row_vertical_divider_header = ft.Row(
                [horizontal_divider_header],
                height=16,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.alignment.bottom_center,
                offset=(0, 1))

    def resize():
        width_page = int(page.width)
        if width_page < 1309:
            horizontal_divider_header.width = width_page - 40
        else:
            horizontal_divider_header.width = 1309

        if width_page < 790:
            row_header.scroll = ft.ScrollMode.ADAPTIVE
        else:
            row_header.scroll = False

    resize()

    async def page_resize(e):
        resize()
        await page.update_async()

    page.on_resize = page_resize

    page.appbar = ft.AppBar(
        title=ft.Column([
            row_header,
            row_vertical_divider_header
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
