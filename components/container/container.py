import copy
import flet as ft

from components.stack.stack import bttn_order_stack, bttn_product_stack, \
    bttn_deliver_stack, bttn_approve_sell_stack, bttn_end_sell_stack, \
    bttn_product_sell_stack, bttn_end_order_required_stack, bttn_end_order_prav_stack, \
    bttn_end_order_assign_driver_stack, bttn_end_order_stack, bttn_sell_stack, \
    bttn_approve_stack, bttn_required_stack, bttn_assign_driver_stack, \
    bttn_end_order_obes_stack
from components.text.text import txt_main_text_order, txt_main_text_sell

container_txt_start_order = ft.Container(
    content=txt_main_text_order,
    margin=20,
    offset=ft.transform.Offset(0, -0.08),
    alignment=ft.alignment.center)

container_txt_start_sell = ft.Container(
    content=txt_main_text_sell,
    margin=20,
    offset=ft.transform.Offset(0, -0.15),
    alignment=ft.alignment.center)


bttn_order_container = ft.Container(bttn_order_stack)
bttn_product_container = ft.Container(bttn_product_stack)
bttn_approve_container = ft.Container(bttn_approve_stack)
bttn_deliver_container = ft.Container(bttn_deliver_stack)
bttn_end_order_container = ft.Container(bttn_end_order_stack)

bttn_sell_container = ft.Container(bttn_sell_stack)
bttn_add_product_container = ft.Container(bttn_approve_sell_stack)
bttn_required_container = ft.Container(bttn_required_stack)
bttn_assign_driver_container = ft.Container(bttn_assign_driver_stack)
bttn_in_work_sell_container = ft.Container(bttn_product_sell_stack)
bttn_driver_in_storage_container = ft.Container(bttn_end_order_required_stack)
bttn_deliver_sell_container = ft.Container(bttn_end_order_prav_stack)
bttn_delivered_sell_container = ft.Container(bttn_end_order_obes_stack)
bttn_sign_docs_container = ft.Container(bttn_end_order_assign_driver_stack)
bttn_end_sell_container = ft.Container(bttn_end_sell_stack)


# empty button
bttn_empty_sample = ft.Container(
        width=75, height=75, disabled=True, visible=True)

bttn_empty = copy.deepcopy(bttn_empty_sample)
bttn_empty_2 = copy.deepcopy(bttn_empty_sample)


# tools page
container_delete_order = ft.Container(
        content=ft.Text(
            value='Удаление заказа',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE),
        margin=20,
        offset=ft.transform.Offset(0, 0.1),
        alignment=ft.alignment.center)

container_choice_tool = ft.Container(
        content=ft.Text(
            value='Выберите инструмент',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE),
        margin=20,
        offset=ft.transform.Offset(0, -0.08),
        alignment=ft.alignment.center)


# autotest page
example_container = ft.Container(margin=ft.margin.only(top=10))


# start.py
horizontal_divider = ft.Container(width=1309, height=1, bgcolor="#857d7f")
