import flet as ft

from components.icon.icon import Icons
from components.text.text import Texts


def info_page(page):

    icon_tg = Icons().icon_tg
    icon_yt = Icons().icon_yt
    txt_tg = Texts().txt_tg
    txt_yt = Texts().txt_yt
    container_app_version = Texts().container_app_version
    container_creator_fio = Texts().txt_creator_fio

    async def press_tg(e):
        await page.launch_url_async('https://t.me/KononovQA')

    async def press_yt(e):
        await page.launch_url_async('https://youtube.com/@KononovQA')

    icon_tg.on_click = press_tg
    icon_yt.on_click = press_yt

    content = ft.Column([
        ft.Row([container_app_version], offset=(0, 0.3),
               alignment=ft.MainAxisAlignment.START),
        ft.Row([container_creator_fio],
               alignment=ft.MainAxisAlignment.START),
        ft.Row([icon_tg, txt_tg], alignment=ft.MainAxisAlignment.START, offset=(0, -0.5)),
        ft.Row([icon_yt, txt_yt], alignment=ft.MainAxisAlignment.START, offset=(0, -0.5))
    ], width=1300, alignment=ft.MainAxisAlignment.CENTER)

    return content
