import flet as ft

from components.icon.icon import Icons
from components.text.text import Texts


def info_page(page):

    icon_tg = Icons().icon_tg
    icon_yt = Icons().icon_yt
    icon_github = Icons().icon_github
    icon_email = Icons().icon_email
    icon_linkedin = Icons().icon_linkedin
    icon_inst = Icons().icon_inst

    txt_tg = Texts().txt_tg
    txt_yt = Texts().txt_yt
    txt_github = Texts().txt_github
    txt_email = Texts().txt_email
    txt_linkedin = Texts().txt_linkedin
    txt_inst = Texts().txt_inst

    container_app_version = Texts().container_app_version
    container_creator_fio = Texts().txt_creator_fio

    async def press_tg(e):
        await page.launch_url_async('https://t.me/KononovQA')

    async def press_yt(e):
        await page.launch_url_async('https://youtube.com/@KononovQA')

    async def press_github(e):
        await page.launch_url_async('https://github.com/kononovqa/flet_qa_helper')

    async def press_email(e):
        await page.set_clipboard_async('mk@kononovqa.ru')

    async def press_linkedin(e):
        await page.launch_url_async('https://linkedin.com/in/kononovqa')

    async def press_inst(e):
        await page.launch_url_async('https://instagram.com/yoshikitzu')

    icon_tg.on_click = press_tg
    icon_yt.on_click = press_yt
    icon_github.on_click = press_github
    icon_email.on_click = press_email
    icon_linkedin.on_click = press_linkedin
    icon_inst.on_click = press_inst

    content = ft.Column([
        ft.Row([container_app_version], offset=(0, 0.3),
               alignment=ft.MainAxisAlignment.START),
        ft.Row([container_creator_fio],
               alignment=ft.MainAxisAlignment.START),
        ft.Row([icon_yt, txt_yt], alignment=ft.MainAxisAlignment.START, offset=(0, -0.5)),
        ft.Row([icon_tg, txt_tg], alignment=ft.MainAxisAlignment.START, offset=(0, -0.5)),
        ft.Row([icon_github, txt_github], alignment=ft.MainAxisAlignment.START,
               offset=(0, -0.5)),
        ft.Row([icon_email, txt_email], alignment=ft.MainAxisAlignment.START,
               offset=(0, -0.5)),
        ft.Row([icon_linkedin, txt_linkedin], alignment=ft.MainAxisAlignment.START,
               offset=(0, -0.5)),
        ft.Row([icon_inst, txt_inst], alignment=ft.MainAxisAlignment.START,
               offset=(0, -0.5))
    ], width=1300, alignment=ft.MainAxisAlignment.CENTER)

    return content
