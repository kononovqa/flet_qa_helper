import copy
import flet as ft

from components.button.styles import button_style_enabled, button_style_disabled
from components.icon.icon import icon_rotate_right, icon_bttn_update, icon_bttn_push, \
        icon_go_to_url, icon_copy_order
from components.text.text import text_in_buttons, create_order_txt, bttn_product_txt, \
        bttn_approve_txt, bttn_deliver_txt, bttn_end_order_txt, bttn_sell_txt, \
        bttn_approve_sell_txt, bttn_required_txt, bttn_assign_driver_txt, \
        bttn_end_order_obes_txt, bttn_end_order_assign_driver_txt, \
        bttn_product_sell_txt, bttn_end_order_required_txt, bttn_end_order_prav_txt, \
        bttn_end_sell_txt

# main buttons
elevated_button_main = ft.ElevatedButton(
        content=text_in_buttons,
        width=220, height=75,
        disabled=True,
        style=button_style_disabled)

bttn_order = copy.deepcopy(elevated_button_main)
bttn_order.style = button_style_enabled
bttn_order.disabled = False
bttn_order.content = create_order_txt

bttn_product = copy.deepcopy(elevated_button_main)
bttn_product.content = bttn_product_txt

bttn_approve = copy.deepcopy(elevated_button_main)
bttn_approve.content = bttn_approve_txt

bttn_deliver = copy.deepcopy(elevated_button_main)
bttn_deliver.content = bttn_deliver_txt

bttn_end_order = copy.deepcopy(elevated_button_main)
bttn_end_order.content = bttn_end_order_txt

bttn_product = copy.deepcopy(elevated_button_main)
bttn_product.content = bttn_product_txt


bttn_sell = copy.deepcopy(elevated_button_main)
bttn_sell.style = button_style_enabled
bttn_sell.disabled = False
bttn_sell.content = bttn_sell_txt

bttn_product_sell = copy.deepcopy(elevated_button_main)
bttn_product_sell.content = bttn_product_sell_txt

bttn_approve_sell = copy.deepcopy(elevated_button_main)
bttn_approve_sell.content = bttn_approve_sell_txt

bttn_required = copy.deepcopy(elevated_button_main)
bttn_required.content = bttn_required_txt

bttn_assign_driver = copy.deepcopy(elevated_button_main)
bttn_assign_driver.content = bttn_assign_driver_txt

bttn_end_order_required = copy.deepcopy(elevated_button_main)
bttn_end_order_required.content = bttn_end_order_required_txt

bttn_end_order_prav = copy.deepcopy(elevated_button_main)
bttn_end_order_prav.content = bttn_end_order_prav_txt

bttn_end_order_obes = copy.deepcopy(elevated_button_main)
bttn_end_order_obes.content = bttn_end_order_obes_txt

bttn_end_order_assign_driver = copy.deepcopy(elevated_button_main)
bttn_end_order_assign_driver.content = bttn_end_order_assign_driver_txt

bttn_end_sell = copy.deepcopy(elevated_button_main)
bttn_end_sell.content = bttn_end_sell_txt


# update and push buttons
elevated_button_square = ft.ElevatedButton(
        content=icon_rotate_right,
        width=75, height=75, style=button_style_disabled, disabled=True)

bttn_update = copy.deepcopy(elevated_button_square)
bttn_update.content = icon_bttn_update

bttn_push = copy.deepcopy(elevated_button_square)
bttn_push.style = button_style_enabled
bttn_push.disabled = False
bttn_push.content = icon_bttn_push


bttn_update_sell = copy.deepcopy(elevated_button_square)
bttn_update_sell.content = icon_bttn_update

bttn_push_sell = copy.deepcopy(elevated_button_square)
bttn_push_sell.style = button_style_enabled
bttn_push_sell.disabled = False
bttn_push_sell.content = icon_bttn_push


# go to url and copy buttons
elevated_button_go_url_and_copy = ft.ElevatedButton(
        width=75, height=55, style=button_style_enabled, disabled=False, visible=False,
        offset=(0, -0.03))

bttn_go_order = copy.deepcopy(elevated_button_go_url_and_copy)
bttn_go_order.content = icon_go_to_url

bttn_go_sell = copy.deepcopy(elevated_button_go_url_and_copy)
bttn_go_sell.content = icon_go_to_url

bttn_copy_str_order = copy.deepcopy(elevated_button_go_url_and_copy)
bttn_copy_str_order.content = icon_copy_order

bttn_copy_str_sell = copy.deepcopy(elevated_button_go_url_and_copy)
bttn_copy_str_sell.content = icon_copy_order


# tools page
bttn_delete_order_go = ft.ElevatedButton(
        content=ft.Icon(name=ft.icons.DELETE),
        width=75, height=55, style=button_style_enabled, disabled=False,
        offset=(0, -0.03))

bttn_delete_order = ft.ElevatedButton(
        content=ft.Text(value="Удалить заказ",
                        text_align=ft.TextAlign.CENTER),
        width=220, height=75, style=button_style_enabled, disabled=False)

bttn_reset_password = ft.ElevatedButton(
        content=ft.Text(value="Сбросить всем пользователям пароли",
                        text_align=ft.TextAlign.CENTER),
        width=220, height=75, style=button_style_enabled, disabled=False)
