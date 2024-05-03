import flet as ft

from components.button.styles import ButtonStyles


class TextFields:
    def __init__(self):

        # text upper url line when press button
        self.txt_line_when_pressed = ft.TextField(
            width=1230, height=55, text_size=13, disabled=False, border_radius=8,
            read_only=True, color=ft.colors.GREY_600, border_color=ft.colors.GREY_700,
            label='', label_style=ButtonStyles().style_txt_label,
            value="", visible=False)

        # tools page
        self.txt_delete_order = ft.TextField(
            width=600, height=55, text_size=13, disabled=False, border_radius=8,
            read_only=False, color=ft.colors.WHITE, border_color=ft.colors.WHITE,
            label='ID Заказа', label_style=ButtonStyles().style_txt_label,
            value="", visible=True)

    def txt_go_order(self):
        self.txt_line_when_pressed.label = 'Ссылка на заказ'
        return self.txt_line_when_pressed

    def txt_go_sell(self):
        self.txt_line_when_pressed.label = 'Ссылка на продажу'
        return self.txt_line_when_pressed

    def txt_creator_order(self):
        self.txt_line_when_pressed.label = 'Создатель заказа'
        return self.txt_line_when_pressed

    def txt_sell_str(self):
        self.txt_line_when_pressed.label = 'Сопровождающий менеджер'
        return self.txt_line_when_pressed
