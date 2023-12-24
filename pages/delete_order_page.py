import flet as ft
import traceback

from components.button.elevated_button import bttn_delete_order_go
from components.button.styles import button_style_disabled, button_style_enabled
from components.container.container import container_delete_order
from components.text_field.text_field import txt_delete_order
from press_button.fake_do_something import do_something


def delete_order_page(page):
    async def delete_order(e):
        try:
            bttn_delete_order_go.disabled = True
            bttn_delete_order_go.style = button_style_disabled
            await page.update_async()
            await do_something()
        except:
            txt_delete_order.border_color = ft.colors.RED
            bttn_delete_order_go.disabled = False
            bttn_delete_order_go.style = button_style_enabled
            await page.update_async()
            traceback.print_exc()
            return 0

        bttn_delete_order_go.disabled = False
        bttn_delete_order_go.style = button_style_enabled
        txt_delete_order.border_color = ft.colors.GREEN
        await page.update_async()

    async def go_white(e):
        txt_delete_order.border_color = ft.colors.WHITE
        await page.update_async()

    txt_delete_order.on_change = go_white
    bttn_delete_order_go.on_click = delete_order

    content = ft.Column([
        container_delete_order,
        ft.Row([txt_delete_order, bttn_delete_order_go],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, 0.3))
    ])

    return content
