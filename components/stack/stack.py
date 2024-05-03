import flet as ft

from components.button.elevated_button import ElevatedButtons
from components.button.icon_button import IconButtons


class Stacks:
    def __init__(self):
        self.stack_main_button = ft.Stack(
            controls=[],
            width=220,
            height=75)
        self.stack_square_button = ft.Stack(
            controls=[],
            width=75,
            height=75)

    def button_order_stack(self):
        button_order = ElevatedButtons().button_order()
        button_icon_settings = IconButtons().button_icon_settings
        self.stack_main_button.controls = [button_order,
                                           button_icon_settings]
        return self.stack_main_button, button_order, button_icon_settings

    def button_product_stack(self):
        button_product = ElevatedButtons().button_product()
        button_repeat_product = IconButtons().button_icon_repeat_one
        self.stack_main_button.controls = [button_product,
                                           button_repeat_product]
        return self.stack_main_button, button_product, button_repeat_product

    def button_approve_stack(self):
        button_approve = ElevatedButtons().button_approve()
        button_repeat_approve = IconButtons().button_icon_repeat_one
        self.stack_main_button.controls = [button_approve,
                                           button_repeat_approve]
        return self.stack_main_button, button_approve, button_repeat_approve

    def button_deliver_stack(self):
        button_deliver = ElevatedButtons().button_deliver()
        button_repeat_deliver = IconButtons().button_icon_repeat_one
        self.stack_main_button.controls = [button_deliver,
                                           button_repeat_deliver]
        return self.stack_main_button, button_deliver, button_repeat_deliver

    def button_deliver_sell_stack(self):
        button_deliver_sell = ElevatedButtons().button_deliver_sell()
        self.stack_main_button.controls = [button_deliver_sell,
                                           IconButtons().button_icon_lock]
        return self.stack_main_button, button_deliver_sell

    def button_delivered_sell_stack(self):
        button_delivered_sell = ElevatedButtons().button_delivered_sell()
        self.stack_main_button.controls = [button_delivered_sell,
                                           IconButtons().button_icon_lock]
        return self.stack_main_button, button_delivered_sell

    def button_end_order_stack(self):
        button_end_order = ElevatedButtons().button_end_order()
        button_repeat_end_order = IconButtons().button_icon_repeat_one
        self.stack_main_button.controls = [button_end_order,
                                           button_repeat_end_order]
        return self.stack_main_button, button_end_order, button_repeat_end_order

    def button_sell_stack(self):
        button_sell = ElevatedButtons().button_sell()
        button_settings_sell = IconButtons().button_icon_settings
        self.stack_main_button.controls = [button_sell,
                                           button_settings_sell]
        return self.stack_main_button, button_sell, button_settings_sell

    def button_add_product_stack(self):
        button_add_product = ElevatedButtons().button_add_product()
        self.stack_main_button.controls = [button_add_product,
                                           IconButtons().button_icon_lock]
        return self.stack_main_button, button_add_product

    def button_required_stack(self):
        button_required = ElevatedButtons().button_required()
        button_repeat_required = IconButtons().button_icon_repeat_one
        self.stack_main_button.controls = [button_required,
                                           button_repeat_required]
        return self.stack_main_button, button_required, button_repeat_required

    def button_assign_driver_stack(self):
        button_assign_driver = ElevatedButtons().button_assign_driver()
        button_repeat_assign_driver = IconButtons().button_icon_repeat_one
        self.stack_main_button.controls = [button_assign_driver,
                                           button_repeat_assign_driver]
        return self.stack_main_button, button_assign_driver, button_repeat_assign_driver

    def button_product_sell_stack(self):
        button_product_sell = ElevatedButtons().button_product_sell()
        self.stack_main_button.controls = [button_product_sell,
                                           IconButtons().button_icon_lock]
        return self.stack_main_button, button_product_sell

    def driver_in_storage_stack(self):
        driver_in_storage = ElevatedButtons().driver_in_storage()
        self.stack_main_button.controls = [driver_in_storage,
                                           IconButtons().button_icon_lock]
        return self.stack_main_button, driver_in_storage

    def button_end_order_assign_driver_stack(self):
        button_end_order_assign_driver = (
            ElevatedButtons().button_end_order_assign_driver())
        self.stack_main_button.controls = [button_end_order_assign_driver,
                                           IconButtons().button_icon_lock]
        return self.stack_main_button, button_end_order_assign_driver

    def button_end_sell_stack(self):
        button_end_sell = ElevatedButtons().button_end_sell()
        self.stack_main_button.controls = [button_end_sell,
                                           IconButtons().button_icon_lock]
        return self.stack_main_button, button_end_sell
