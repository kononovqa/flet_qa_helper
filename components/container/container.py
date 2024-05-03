import flet as ft

from components.stack.stack import Stacks
from components.text.text import Texts


class Containers:
    def __init__(self):
        self.empty_container = ft.Container()

        self.container_start = ft.Container(
            margin=20,
            alignment=ft.alignment.center)

        self.button_empty_sample = ft.Container(
            width=75,
            height=75,
            disabled=True,
            visible=True)

        self.container_delete_order = ft.Container(
            content=ft.Text(
                value='Удаление заказа',
                font_family='Arial',
                size=20,
                color=ft.colors.WHITE),
            margin=20,
            offset=ft.transform.Offset(0, 0.1),
            alignment=ft.alignment.center)

        # tools page
        self.container_choice_tool = ft.Container(
            content=ft.Text(
                value='Выберите инструмент',
                font_family='Arial',
                size=20,
                color=ft.colors.WHITE),
            margin=20,
            offset=ft.transform.Offset(0, -0.081),
            alignment=ft.alignment.center)

        # autotest page
        self.example_container = ft.Container(
            margin=ft.margin.only(top=10))

        # start.py
        self.horizontal_divider = ft.Container(
            width=1309,
            height=1,
            bgcolor="#857d7f")

    def button_order_container(self):
        self.empty_container.content, button_order, button_icon_settings = (
            Stacks().button_order_stack())
        return self.empty_container, button_order, button_icon_settings

    def button_product_container(self):
        button_product_stack, button_product, button_repeat_product = (
            Stacks().button_product_stack())
        self.empty_container.content = button_product_stack
        return (self.empty_container, button_product,
                button_repeat_product)

    def button_approve_container(self):
        button_approve_stack, button_approve, button_repeat_approve = (
            Stacks().button_approve_stack())
        self.empty_container.content = button_approve_stack
        return self.empty_container, button_approve, button_repeat_approve

    def button_deliver_container(self):
        button_deliver_stack, button_deliver, button_repeat_deliver = (
            Stacks().button_deliver_stack())
        self.empty_container.content = button_deliver_stack
        return self.empty_container, button_deliver, button_repeat_deliver

    def button_deliver_sell_container(self):
        button_deliver_sell_stack, button_deliver_sell = (
            Stacks().button_deliver_sell_stack())
        self.empty_container.content = button_deliver_sell_stack
        return self.empty_container, button_deliver_sell

    def button_delivered_sell_container(self):
        button_delivered_sell_stack, button_delivered_sell = (
            Stacks().button_delivered_sell_stack())
        self.empty_container.content = button_delivered_sell_stack
        return self.empty_container, button_delivered_sell

    def button_end_order_container(self):
        button_end_order_stack, button_end_order, button_repeat_end_order = (
            Stacks().button_end_order_stack())
        self.empty_container.content = button_end_order_stack
        return (self.empty_container, button_end_order,
                button_repeat_end_order)

    def button_sell_container(self):
        button_sell_stack, button_sell, button_settings_sell = (
            Stacks().button_sell_stack())
        self.empty_container.content = button_sell_stack
        return self.empty_container, button_sell, button_settings_sell

    def button_add_product_container(self):
        button_add_product_stack, button_add_product = Stacks().button_add_product_stack()
        self.empty_container.content = button_add_product_stack
        return self.empty_container, button_add_product

    def button_required_container(self):
        button_required_stack, button_required, button_repeat_required = (
            Stacks().button_required_stack())
        self.empty_container.content = button_required_stack
        return self.empty_container, button_required, button_repeat_required

    def button_assign_driver_container(self):
        button_assign_driver_stack, button_assign_driver, button_repeat_assign_driver = (
            Stacks().button_assign_driver_stack())
        self.empty_container.content = button_assign_driver_stack
        return self.empty_container, button_assign_driver, button_repeat_assign_driver

    def button_product_sell_container(self):
        button_product_sell_stack, button_product_sell = (
            Stacks().button_product_sell_stack())
        self.empty_container.content = button_product_sell_stack
        return self.empty_container, button_product_sell

    def button_driver_in_storage_container(self):
        driver_in_storage_stack, driver_in_storage = Stacks().driver_in_storage_stack()
        self.empty_container.content = driver_in_storage_stack
        return self.empty_container, driver_in_storage

    def button_end_order_assign_driver_container(self):
        button_end_order_assign_driver_stack, button_end_order_assign_driver = (
            Stacks().button_end_order_assign_driver_stack())
        self.empty_container.content = button_end_order_assign_driver_stack
        return self.empty_container, button_end_order_assign_driver

    def button_end_sell_container(self):
        button_end_sell_stack, button_end_sell = Stacks().button_end_sell_stack()
        self.empty_container.content = button_end_sell_stack
        return self.empty_container, button_end_sell

    def container_txt_start_order(self):
        txt_main_text_order = Texts().txt_main_text_order()
        self.container_start.offset = ft.transform.Offset(0, -0.08)
        self.container_start.content = txt_main_text_order
        return self.container_start, txt_main_text_order

    def container_txt_start_sell(self):
        txt_main_text_sell = Texts().txt_main_text_sell()
        self.container_start.offset = ft.transform.Offset(0, -0.15)
        self.container_start.content = txt_main_text_sell
        return self.container_start, txt_main_text_sell
