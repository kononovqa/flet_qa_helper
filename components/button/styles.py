import flet as ft

button_style_enabled = ft.ButtonStyle(color=ft.colors.CYAN,
                                      shape=ft.RoundedRectangleBorder(radius=8))

button_style_disabled = ft.ButtonStyle(color=ft.colors.GREY,
                                       shape=ft.RoundedRectangleBorder(radius=8))

button_style_pressed_wait = ft.ButtonStyle(color=ft.colors.BLACK,
                                           bgcolor=ft.colors.YELLOW,
                                           shape=ft.RoundedRectangleBorder(radius=8))

button_style_pressed_access = ft.ButtonStyle(color=ft.colors.GREEN,
                                             bgcolor='#272e29',
                                             shape=ft.RoundedRectangleBorder(radius=8))

button_style_failed_disabled = ft.ButtonStyle(color=ft.colors.RED,
                                              bgcolor='#5e0c06',
                                              shape=ft.RoundedRectangleBorder(radius=8))
