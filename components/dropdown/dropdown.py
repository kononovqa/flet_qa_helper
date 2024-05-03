import flet as ft


class Dropdowns:
    def __init__(self):
        self.dropdown = ft.Dropdown(
            width=700,
            label='Пользователь',
            hint_text="Случайный",
            options=[])

    def dropdown_users(self):
        return self.dropdown
