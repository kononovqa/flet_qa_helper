import copy

import flet as ft

progress_bar = ft.ProgressBar(width=1310,
                              height=8,
                              color=ft.colors.GREEN,
                              bgcolor=ft.colors.CYAN,
                              offset=ft.transform.Offset(0, -0.5),
                              visible=False,
                              value=0)

vertical_divider = ft.ProgressBar(width=1, height=22, value=1, color="#857d7f")

progress_bar_order = copy.deepcopy(progress_bar)
progress_bar_sell = copy.deepcopy(progress_bar)
