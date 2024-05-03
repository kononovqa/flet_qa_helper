import flet as ft


class Rows:
    def __init__(self):
        self.example_raw_with_linechart = ft.Row(
            [],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.END,
            width=1309,
            height=400)

        self.example_raw_between_linecharts = ft.Row([],
                                                     width=1309,
                                                     height=110)
