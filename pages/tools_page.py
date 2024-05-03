import traceback
import asyncio
import flet as ft

from components.button.elevated_button import ElevatedButtons
from components.button.styles import ButtonStyles
from components.container.container import Containers
from components.text.text import Texts

from press_button.fake_do_something import do_something


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

    content = ft.Column([
        container_choice_tool,
        ft.Row([button_delete_order, button_reset_password],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, -0.17)),
        ft.Row([txt_progress_reset_password],
               alignment=ft.MainAxisAlignment.CENTER,
               offset=(0, -0.9))
    ])

    return content
