import flet as ft

example_linechart = ft.LineChart(
        data_series=[],
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.GREY))
        ),
        left_axis=ft.ChartAxis(labels=[],
                               labels_size=50,
                               labels_interval=1),
        bottom_axis=ft.ChartAxis(),
        top_axis=ft.ChartAxis(),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=0,
        min_x=0,
        max_x=0,
        expand=True,
        width=1309,
        height=350
    )
