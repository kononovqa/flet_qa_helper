import traceback
import asyncio
import flet as ft

from components.button.elevated_button import ElevatedButtons
from components.button.styles import ButtonStyles
from components.container.container import Containers
from components.text.text import Texts

from autotest_requests.fake_do_something import do_something


def tools_page(page):
    button_reset_password = ElevatedButtons().button_reset_password()
    txt_progress_reset_password = Texts().text_button_reset_password()
    button_delete_order = ElevatedButtons().button_delete_order()
    container_choice_tool = Containers().container_choice_tool

    async def go_delete_order(e):
        await page.go_async('/tools/delete_order')

    async def go_default_password(e):
        button_reset_password.style = (
            ButtonStyles().button_style_pressed_wait)
        button_reset_password.disabled = True
        await page.update_async()

        try:
            for user in range(0, 10):
                await do_something()
                txt_progress_reset_password.value = f'Сброшен пользователь {user}_name'
                txt_progress_reset_password.visible = True
                await page.update_async()
        except:
            print(f'Ошибка : \n {traceback.format_exc()}')
            button_reset_password.style = ButtonStyles().button_style_failed_disabled
            button_reset_password.disabled = False
            await page.update_async()
        else:
            button_reset_password.style = ButtonStyles().button_style_pressed_access
            button_reset_password.disabled = False
            await page.update_async()
        finally:
            await asyncio.sleep(5)
            button_reset_password.style = ButtonStyles().button_style_enabled
            button_reset_password.disabled = False
            txt_progress_reset_password.value = ''
            await page.update_async()

    button_delete_order.on_click = go_delete_order
    button_reset_password.on_click = go_default_password

    row_options = ft.Row([button_delete_order, button_reset_password],
                         alignment=ft.MainAxisAlignment.CENTER,
                         vertical_alignment=ft.CrossAxisAlignment.CENTER,
                         offset=(0, -0.17))

    def resize():
        width_page = int(page.width)
        if width_page < 470:
            width_button = (width_page - 30) / 2
            if width_button <= 155:
                width_button = 155
            row_options.scroll = ft.ScrollMode.ADAPTIVE
            button_delete_order.width = width_button
            button_reset_password.width = width_button
        else:
            row_options.scroll = False
            button_delete_order.width = 220
            button_reset_password.width = 220

    resize()

    async def page_resize(e):
        resize()
        await page.update_async()

    page.on_resize = page_resize

    content = ft.Column([
        container_choice_tool,
        row_options,
        ft.Row([txt_progress_reset_password],
               alignment=ft.MainAxisAlignment.CENTER,
               offset=(0, -0.9))
    ])

    return content
