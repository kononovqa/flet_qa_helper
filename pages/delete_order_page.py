import flet as ft
import traceback

from components.button.elevated_button import ElevatedButtons
from components.button.styles import ButtonStyles
from components.container.container import Containers
from components.text.text_field import TextFields

from press_button.fake_do_something import do_something


def delete_order_page(page):

    button_delete_order_go = ElevatedButtons().button_delete_order_go()
    container_delete_order = Containers().container_delete_order
    txt_delete_order = TextFields().txt_delete_order

    async def delete_order(e):
        try:
            button_delete_order_go.disabled = True
            button_delete_order_go.style = ButtonStyles().button_style_disabled
            await page.update_async()
            await do_something()
        except:
            txt_delete_order.border_color = ft.colors.RED
            button_delete_order_go.disabled = False
            button_delete_order_go.style = ButtonStyles().button_style_enabled
            await page.update_async()
            traceback.print_exc()
            return 0

        button_delete_order_go.disabled = False
        button_delete_order_go.style = ButtonStyles().button_style_enabled
        txt_delete_order.border_color = ft.colors.GREEN
        await page.update_async()

    async def go_white(e):
        txt_delete_order.border_color = ft.colors.WHITE
        await page.update_async()

    txt_delete_order.on_change = go_white
    button_delete_order_go.on_click = delete_order

    def resize():
        width_page = int(page.width)
        if width_page < 701:
            txt_delete_order_width = (width_page - 75 - 26)
        else:
            txt_delete_order_width = 600
        txt_delete_order.width = txt_delete_order_width
    resize()

    async def page_resize(e):
        resize()
        await page.update_async()

    page.on_resize = page_resize

    content = ft.Column([
        container_delete_order,
        ft.Row([txt_delete_order, button_delete_order_go],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, 0.3))
    ])

    return content
