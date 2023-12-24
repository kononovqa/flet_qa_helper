import flet as ft

from components.icon.icon import icon_tg, icon_yt
from components.text.text import container_app_version, txt_tg, txt_yt


def info_page(page):

    async def press_tg(e):
        await page.launch_url_async('https://t.me/KononovQA')

    async def press_yt(e):
        await page.launch_url_async('https://youtube.com/@KononovQA')

    icon_tg.on_click = press_tg
    icon_yt.on_click = press_yt

    content = ft.Column([
        ft.Row([container_app_version], offset=(0, 0.3),
               alignment=ft.MainAxisAlignment.START),
        ft.Row([icon_tg, txt_tg], alignment=ft.MainAxisAlignment.START),
        ft.Row([icon_yt, txt_yt], alignment=ft.MainAxisAlignment.START)
    ], width=1309, alignment=ft.MainAxisAlignment.CENTER)

    return content
