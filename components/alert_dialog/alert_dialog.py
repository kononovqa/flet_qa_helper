import flet as ft

from components.dropdown.dropdown import dropdown_users_order, dropdown_users_sell

dlg_order = ft.AlertDialog(
        title=ft.Text("Выберите владельца заказа"),
        actions=[dropdown_users_order])

dlg_sell = ft.AlertDialog(
    title=ft.Text("Выберите владельца продажи"),
    actions=[dropdown_users_sell])
