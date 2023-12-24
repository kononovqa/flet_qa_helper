import traceback
import asyncio
import flet as ft

from components.button.elevated_button import bttn_delete_order, bttn_reset_password
from components.button.styles import button_style_pressed_wait, \
    button_style_pressed_access, button_style_failed_disabled, button_style_enabled
from components.container.container import container_choice_tool
from components.text.text import txt_progress_reset_password
from press_button.fake_do_something import do_something


def tools_page(page):
    async def go_delete_order(e):
        await page.go_async('/tools/delete_order')

    async def go_default_password(e):
        bttn_reset_password.style = button_style_pressed_wait
        bttn_reset_password.disabled = True
        await page.update_async()

        try:
            for user in range(0, 10):
                await do_something()
                txt_progress_reset_password.value = f'Сброшен пользователь {user}_name'
                await page.update_async()
        except:
            print(f'Ошибка : \n {traceback.format_exc()}')
            bttn_reset_password.style = button_style_failed_disabled
            bttn_reset_password.disabled = False
            await page.update_async()
        else:
            bttn_reset_password.style = button_style_pressed_access
            bttn_reset_password.disabled = False
            await page.update_async()
        finally:
            await asyncio.sleep(5)
            bttn_reset_password.style = button_style_enabled
            bttn_reset_password.disabled = False
            txt_progress_reset_password.value = ''
            await page.update_async()

    bttn_delete_order.on_click = go_delete_order
    bttn_reset_password.on_click = go_default_password

    content = ft.Column([
        container_choice_tool,
        ft.Row([bttn_delete_order, bttn_reset_password],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, -0.17)),
        ft.Row([txt_progress_reset_password],
               alignment=ft.MainAxisAlignment.CENTER,
               offset=(0, -0.9))
    ])

    return content
