import copy
import flet as ft


dropdown = ft.Dropdown(
    width=700,
    label='Пользователь',
    hint_text="Случайный",
    options=[])


dropdown_users_order = copy.deepcopy(dropdown)
dropdown_users_sell = copy.deepcopy(dropdown)
