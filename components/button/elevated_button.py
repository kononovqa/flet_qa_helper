import flet as ft

from components.button.styles import ButtonStyles
from components.icon.icon import Icons
from components.text.text import Texts


class ElevatedButtons:
    def __init__(self):
        # main big buttons
        self.elevated_button_main = ft.ElevatedButton(
            content=Texts().text_in_buttons,
            width=220,
            height=75,
            disabled=True,
            style=ButtonStyles().button_style_disabled)

        # square buttons
        self.elevated_button_square = ft.ElevatedButton(
            content=Icons().icon_rotate_right,
            width=75,
            height=75,
            style=ButtonStyles().button_style_disabled,
            disabled=True)

        # helper buttons
        self.elevated_button_helpers = ft.ElevatedButton(
            width=75,
            height=55,
            style=ButtonStyles().button_style_enabled,
            disabled=False,
            visible=False,
            offset=(0, -0.03))

    # tools page
    def button_delete_order_go(self):
        self.elevated_button_helpers.content = Icons().icon_delete
        self.elevated_button_helpers.visible = True
        return self.elevated_button_helpers

    def button_delete_order(self):
        self.elevated_button_main.content = Texts().text_delete_order()
        self.elevated_button_main.style = ButtonStyles().button_style_enabled
        self.elevated_button_main.disabled = False
        return self.elevated_button_main

    def button_reset_password(self):
        self.elevated_button_main.content = Texts().text_button_reset_password()
        self.elevated_button_main.style = ButtonStyles().button_style_enabled
        self.elevated_button_main.disabled = False
        return self.elevated_button_main

    def button_order(self):
        self.elevated_button_main.style = ButtonStyles().button_style_enabled
        self.elevated_button_main.disabled = False
        self.elevated_button_main.content = Texts().create_order_txt()
        return self.elevated_button_main

    def button_product(self):
        self.elevated_button_main.content = Texts().button_product_txt()
        return self.elevated_button_main

    def button_approve(self):
        self.elevated_button_main.content = Texts().button_approve_txt()
        return self.elevated_button_main

    def button_deliver(self):
        self.elevated_button_main.content = Texts().button_deliver_txt()
        return self.elevated_button_main

    def button_end_order(self):
        self.elevated_button_main.content = Texts().button_end_order_txt()
        return self.elevated_button_main

    def button_sell(self):
        self.elevated_button_main.style = ButtonStyles().button_style_enabled
        self.elevated_button_main.disabled = False
        self.elevated_button_main.content = Texts().button_sell_txt()
        return self.elevated_button_main

    def button_product_sell(self):
        self.elevated_button_main.content = Texts().button_product_sell_txt()
        return self.elevated_button_main

    def button_add_product(self):
        self.elevated_button_main.content = Texts().button_add_product_txt()
        return self.elevated_button_main

    def button_required(self):
        self.elevated_button_main.content = Texts().button_required_txt()
        return self.elevated_button_main

    def button_assign_driver(self):
        self.elevated_button_main.content = Texts().button_assign_driver_txt()
        return self.elevated_button_main

    def driver_in_storage(self):
        self.elevated_button_main.content = Texts().driver_in_storage_txt()
        return self.elevated_button_main

    def button_deliver_sell(self):
        self.elevated_button_main.content = Texts().button_deliver_sell_txt()
        return self.elevated_button_main

    def button_delivered_sell(self):
        self.elevated_button_main.content = Texts().button_delivered_sell_txt()
        return self.elevated_button_main

    def button_end_order_assign_driver(self):
        self.elevated_button_main.content = Texts().button_end_order_assign_driver_txt()
        return self.elevated_button_main

    def button_end_sell(self):
        self.elevated_button_main.content = Texts().button_end_sell_txt()
        return self.elevated_button_main

    def button_update(self):
        self.elevated_button_square.content = Icons().icon_rotate_right
        return self.elevated_button_square

    def button_push(self):
        self.elevated_button_square.style = ButtonStyles().button_style_enabled
        self.elevated_button_square.disabled = False
        self.elevated_button_square.content = Icons().icon_push
        return self.elevated_button_square

    def button_go_to_link(self):
        self.elevated_button_helpers.content = Icons().icon_send
        return self.elevated_button_helpers

    def button_copy(self):
        self.elevated_button_helpers.content = Icons().icon_copy
        return self.elevated_button_helpers
