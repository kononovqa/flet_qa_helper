import flet as ft

from components.dropdown.dropdown import Dropdowns
from components.text.text import Texts


class AlertDialogs:
    def __init__(self):
        # main text
        self.alert_dialog = ft.AlertDialog()

    def dialog_order(self):
        self.alert_dialog.title = Texts().dialog_order_txt()
        dropdown = Dropdowns().dropdown_users()
        self.alert_dialog.actions = [dropdown]
        return self.alert_dialog, dropdown

    def dialog_sell(self):
        self.alert_dialog.title = Texts().dialog_sell_txt()
        dropdown = Dropdowns().dropdown_users()
        self.alert_dialog.actions = [dropdown]
        return self.alert_dialog, dropdown
