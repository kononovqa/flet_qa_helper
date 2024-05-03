import flet as ft

from components.text.text import Texts


def stands_page(page):
    stands_header = Texts().stands_header()
    stands_1 = Texts().stands_1()
    stands_2 = Texts().stands_2()
    stands_3 = Texts().stands_3()
    stands_4 = Texts().stands_4()
    stands_5 = Texts().stands_5()
    stands_6 = Texts().stands_6()
    stands_7 = Texts().stands_7()
    stands_8 = Texts().stands_8()

    page.scroll = 'AUTO'

    datatable = ft.DataTable(data_row_max_height=60, offset=(0, 0.02), columns=[
        ft.DataColumn(stands_header),
        ft.DataColumn(stands_1),
        ft.DataColumn(stands_2),
        ft.DataColumn(stands_3),
        ft.DataColumn(stands_4),
        ft.DataColumn(stands_5),
        ft.DataColumn(stands_6),
        ft.DataColumn(stands_7),
        ft.DataColumn(stands_8)
    ],
     rows=[
         ft.DataRow(
             cells=[
                 ft.DataCell(
                     ft.Text("SERVICE 1", size=15, weight=ft.FontWeight.BOLD,
                             width=100,
                             text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 1 STAND 1",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 1 STAND 2",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 1 STAND 3",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 1 STAND 4",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 1 STAND 5",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 1 STAND 6",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text('---', width=89, text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text('---', width=89, text_align=ft.TextAlign.CENTER))
             ],
         ),
         ft.DataRow(
             cells=[
                 ft.DataCell(ft.Text("SERVICE 2", size=15, weight=ft.FontWeight.BOLD,
                                     width=100,
                                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 2 STAND 1",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text('---', width=89,
                                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 2 STAND 3",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 2 STAND 4",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 2 STAND 5",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 2 STAND 6",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text('---', width=89,
                                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text('---', width=89,
                                     text_align=ft.TextAlign.CENTER))
             ],
         ),
         ft.DataRow(
             cells=[
                 ft.DataCell(ft.Text("SERVICE 3", size=15,
                                     weight=ft.FontWeight.BOLD, width=100,
                                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 3 STAND 1",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 3 STAND 2",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 3 STAND 3",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 3 STAND 4",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 3 STAND 5",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 3 STAND 6",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 3 STAND 7",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 3 STAND 8",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER))
             ],
         ),
         ft.DataRow(
             cells=[
                 ft.DataCell(
                     ft.Text("SERVICE 4", size=15, weight=ft.FontWeight.BOLD, width=100,
                             text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 4 STAND 1",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 4 STAND 2",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 4 STAND 3",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 4 STAND 4",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 4 STAND 5",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text(spans=[ft.TextSpan(
                     "SERVICE 4 STAND 6",
                     url='https://www.google.ru/',
                     style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                     text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text('---', width=89, text_align=ft.TextAlign.CENTER)),
                 ft.DataCell(ft.Text('---', width=89, text_align=ft.TextAlign.CENTER))
             ],
         ),
     ]
     )

    datatable_services = ft.DataTable(width=1309, data_row_max_height=70, columns=[
        ft.DataColumn(stands_header),
        ft.DataColumn(stands_1),
        ft.DataColumn(stands_2),
        ft.DataColumn(stands_3),
        ft.DataColumn(stands_4),
        ft.DataColumn(stands_5),
        ft.DataColumn(stands_6)
    ], rows=[ft.DataRow(
        cells=[
            ft.DataCell(
                ft.Text("SERVICE 1", size=15, weight=ft.FontWeight.BOLD, width=100,
                        text_align=ft.TextAlign.CENTER)),
            ft.DataCell(ft.Text(spans=[ft.TextSpan(
                "SWAGGER STAND 1",
                url='https://www.google.ru/',
                style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                text_align=ft.TextAlign.CENTER)),
            ft.DataCell(ft.Text(spans=[ft.TextSpan(
                "SWAGGER STAND 2",
                url='https://www.google.ru/',
                style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                text_align=ft.TextAlign.CENTER)),
            ft.DataCell(ft.Text(spans=[ft.TextSpan(
                "SWAGGER STAND 3",
                url='https://www.google.ru/',
                style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                text_align=ft.TextAlign.CENTER)),
            ft.DataCell(ft.Text(spans=[ft.TextSpan(
                "SWAGGER STAND 4",
                url='https://www.google.ru/',
                style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                text_align=ft.TextAlign.CENTER)),
            ft.DataCell(ft.Text(spans=[ft.TextSpan(
                "SWAGGER STAND 5",
                url='https://www.google.ru/',
                style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                text_align=ft.TextAlign.CENTER)),
            ft.DataCell(ft.Text(spans=[ft.TextSpan(
                "SWAGGER STAND 6",
                url='https://www.google.ru/',
                style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                text_align=ft.TextAlign.CENTER))
        ],
    ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("SERVICE 2", size=15, weight=ft.FontWeight.BOLD,
                                    width=100,
                                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 1",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 2",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 3",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 4",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 5",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 6",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER))
            ],
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("SERVICE 3", size=15,
                                    weight=ft.FontWeight.BOLD, width=100,
                                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 1",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 2",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 3",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 4",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 5",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 6",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER))
            ],
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text("SERVICE 4", size=15, weight=ft.FontWeight.BOLD,
                            width=100,
                            text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 1",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 2",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 3",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 4",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 5",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 6",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER))
            ],
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text("SERVICE 5", size=15, weight=ft.FontWeight.BOLD,
                            width=100,
                            text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 1",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 2",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 3",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 4",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 5",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 6",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER))
            ],
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(
                    ft.Text("SERVICE 6", size=15, weight=ft.FontWeight.BOLD,
                            width=100,
                            text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 1",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 2",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 3",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 4",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 5",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER)),
                ft.DataCell(ft.Text(spans=[ft.TextSpan(
                    "SWAGGER STAND 6",
                    url='https://www.google.ru/',
                    style=ft.TextStyle(color=ft.colors.CYAN))], width=89,
                    text_align=ft.TextAlign.CENTER))
            ],
        ),
    ])

    content = ft.Column([ft.Row([
        datatable
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    ),
        ft.Row([],
               width=1309,
               height=80
               ),
        ft.Row([
            datatable_services
        ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )])

    return content
