import copy
import flet as ft

from components.text.styles import style_txt_label


# text upper url line when press button
txt_line_when_pressed = ft.TextField(
    width=1230, height=55, text_size=13, disabled=False, border_radius=8,
    read_only=True, color=ft.colors.GREY_600, border_color=ft.colors.GREY_700,
    label='', label_style=style_txt_label,
    value="", visible=False)

txt_go_order = copy.deepcopy(txt_line_when_pressed)
txt_go_order.label = 'Ссылка на заказ'

txt_go_sell = copy.deepcopy(txt_line_when_pressed)
txt_go_sell.label = 'Ссылка на продажу'

txt_creator_order = copy.deepcopy(txt_line_when_pressed)
txt_creator_order.label = 'Создатель заказа'

txt_sell_str = copy.deepcopy(txt_line_when_pressed)
txt_sell_str.label = 'Сопровождающий менеджер'


# tools page
txt_delete_order = ft.TextField(
        width=600, height=55, text_size=13, disabled=False, border_radius=8,
        read_only=False, color=ft.colors.WHITE, border_color=ft.colors.WHITE,
        label='ID Заказа', label_style=style_txt_label,
        value="", visible=True)
