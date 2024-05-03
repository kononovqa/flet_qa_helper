import flet as ft


class LineChartDatas:
    def __init__(self):
        self.example_data_points = ft.LineChartData(
            data_points=[],
            stroke_width=3,
            color=ft.colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
            below_line_bgcolor=ft.colors.with_opacity(0.5, ft.colors.LIGHT_GREEN),
            point=True
        )
