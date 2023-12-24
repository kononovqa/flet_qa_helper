import copy
import flet as ft

icon_rotate_right = ft.Icon(name=ft.icons.ROTATE_RIGHT)
icon_push = ft.Icon(name=ft.icons.FAST_FORWARD)
icon_send = ft.Icon(name=ft.icons.SEND)
icon_copy = ft.Icon(name=ft.icons.COPY)
icon_tg = ft.IconButton(icon=ft.icons.TELEGRAM,
                        icon_color=ft.colors.WHITE)
icon_yt = ft.IconButton(icon=ft.icons.ONDEMAND_VIDEO,
                        icon_color=ft.colors.WHITE)

icon_bttn_update = copy.deepcopy(icon_rotate_right)

icon_bttn_push = copy.deepcopy(icon_push)

icon_go_to_url = copy.deepcopy(icon_send)

icon_copy_order = copy.deepcopy(icon_copy)
