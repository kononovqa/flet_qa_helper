import copy
import flet as ft

from components.button.elevated_button import bttn_order, bttn_product, bttn_approve, \
    bttn_end_order, bttn_sell, bttn_approve_sell, bttn_required, bttn_assign_driver, \
    bttn_end_order_prav, bttn_end_order_obes, bttn_end_order_assign_driver, \
    bttn_deliver, bttn_product_sell, bttn_end_order_required, bttn_end_order, \
    bttn_end_sell
from components.button.icon_button import bttn_settings, bttn_repeat_product, \
    bttn_repeat_deliver, icon_lock, bttn_settings_sell, bttn_repeat_required, \
    bttn_repeat_end_order, bttn_repeat_approve, bttn_repeat_assign_driver

stack_main_button = ft.Stack(controls=[], width=220, height=75)
stack_square_button = ft.Stack(controls=[], width=75, height=75)


bttn_order_stack = copy.deepcopy(stack_main_button)
bttn_order_stack.controls = [bttn_order, bttn_settings]

bttn_product_stack = copy.deepcopy(stack_main_button)
bttn_product_stack.controls = [bttn_product, bttn_repeat_product]

bttn_approve_stack = copy.deepcopy(stack_main_button)
bttn_approve_stack.controls = [bttn_approve, bttn_repeat_approve]

bttn_deliver_stack = copy.deepcopy(stack_main_button)
bttn_deliver_stack.controls = [bttn_deliver, bttn_repeat_deliver]

bttn_end_order_stack = copy.deepcopy(stack_main_button)
bttn_end_order_stack.controls = [bttn_end_order, bttn_repeat_end_order]


bttn_sell_stack = copy.deepcopy(stack_main_button)
bttn_sell_stack.controls = [bttn_sell, bttn_settings_sell]

bttn_approve_sell_stack = copy.deepcopy(stack_main_button)
bttn_approve_sell_stack.controls = [bttn_approve_sell, copy.deepcopy(icon_lock)]

bttn_required_stack = copy.deepcopy(stack_main_button)
bttn_required_stack.controls = [bttn_required, bttn_repeat_required]

bttn_assign_driver_stack = copy.deepcopy(stack_main_button)
bttn_assign_driver_stack.controls = [bttn_assign_driver, bttn_repeat_assign_driver]

bttn_product_sell_stack = copy.deepcopy(stack_main_button)
bttn_product_sell_stack.controls = [bttn_product_sell, copy.deepcopy(icon_lock)]

bttn_end_order_required_stack = copy.deepcopy(stack_main_button)
bttn_end_order_required_stack.controls = [bttn_end_order_required, copy.deepcopy(icon_lock)]

bttn_end_order_prav_stack = copy.deepcopy(stack_main_button)
bttn_end_order_prav_stack.controls = [bttn_end_order_prav, copy.deepcopy(icon_lock)]

bttn_end_order_obes_stack = copy.deepcopy(stack_main_button)
bttn_end_order_obes_stack.controls = [bttn_end_order_obes, copy.deepcopy(icon_lock)]

bttn_end_order_assign_driver_stack = copy.deepcopy(stack_main_button)
bttn_end_order_assign_driver_stack.controls = [bttn_end_order_assign_driver, copy.deepcopy(icon_lock)]

bttn_end_sell_stack = copy.deepcopy(stack_main_button)
bttn_end_sell_stack.controls = [bttn_end_sell, copy.deepcopy(icon_lock)]

