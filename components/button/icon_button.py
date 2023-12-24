import copy
import flet as ft

from components.button.styles import button_style_disabled, button_style_enabled

icon_lock = ft.IconButton(icon=ft.icons.LOCK_OUTLINED,
                          icon_color=ft.colors.GREY_500,
                          disabled=True, bottom=0, right=0)

icon_repeat_one = ft.IconButton(icon=ft.icons.REPEAT_ONE,
                                style=button_style_disabled,
                                disabled=True, top=0, right=0,
                                offset=(0.1, -0.1))

icon_settings = ft.IconButton(icon=ft.icons.SETTINGS,
                              style=button_style_enabled,
                              disabled=False,
                              top=0,
                              right=0,
                              offset=(0.1, -0.1))

bttn_repeat_deliver = copy.deepcopy(icon_repeat_one)
bttn_repeat_approve = copy.deepcopy(icon_repeat_one)
bttn_repeat_product = copy.deepcopy(icon_repeat_one)
bttn_repeat_assign_driver = copy.deepcopy(icon_repeat_one)
bttn_repeat_required = copy.deepcopy(icon_repeat_one)
bttn_repeat_end_order = copy.deepcopy(icon_repeat_one)

bttn_settings = copy.deepcopy(icon_settings)
bttn_settings_sell = copy.deepcopy(icon_settings)
