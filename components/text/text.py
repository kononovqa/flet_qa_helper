import copy
import flet as ft

from components.text_span.text_span import example_textspan

# main text
txt_main_text = ft.Text(value='',
                        font_family='Arial',
                        size=20,
                        color=ft.colors.WHITE)

txt_main_text_sell = copy.deepcopy(txt_main_text)
txt_main_text_sell.value = 'Создайте продажу'

txt_main_text_order = copy.deepcopy(txt_main_text)
txt_main_text_order.value = 'Создайте заказ'

# text in buttons
text_in_buttons = ft.Text(value='',
                          text_align=ft.TextAlign.CENTER)

create_order_txt = copy.deepcopy(text_in_buttons)
create_order_txt.value = 'Создать новый заказ'

bttn_product_txt = copy.deepcopy(text_in_buttons)
bttn_product_txt.value = 'Выбрать случайного поставщика и товар'

bttn_approve_txt = copy.deepcopy(text_in_buttons)
bttn_approve_txt.value = 'Согласовать'

bttn_deliver_txt = copy.deepcopy(text_in_buttons)
bttn_deliver_txt.value = 'Доставить'

bttn_end_order_txt = copy.deepcopy(text_in_buttons)
bttn_end_order_txt.value = 'Завершить заказ'

bttn_sell_txt = copy.deepcopy(text_in_buttons)
bttn_sell_txt.value = 'Создать продажу'

bttn_product_sell_txt = copy.deepcopy(text_in_buttons)
bttn_product_sell_txt.value = 'В работе'

bttn_approve_sell_txt = copy.deepcopy(text_in_buttons)
bttn_approve_sell_txt.value = 'Добавить товары'

bttn_required_txt = copy.deepcopy(text_in_buttons)
bttn_required_txt.value = 'Заполнить обязательные поля'

bttn_assign_driver_txt = copy.deepcopy(text_in_buttons)
bttn_assign_driver_txt.value = 'Назначить водителя'

bttn_end_order_required_txt = copy.deepcopy(text_in_buttons)
bttn_end_order_required_txt.value = 'Водитель на складе'

bttn_end_order_prav_txt = copy.deepcopy(text_in_buttons)
bttn_end_order_prav_txt.value = 'Доставка'

bttn_end_order_obes_txt = copy.deepcopy(text_in_buttons)
bttn_end_order_obes_txt.value = 'Доставлено'

bttn_end_order_assign_driver_txt = copy.deepcopy(text_in_buttons)
bttn_end_order_assign_driver_txt.value = 'Заполнить закрывающие документы'

bttn_end_sell_txt = copy.deepcopy(text_in_buttons)
bttn_end_sell_txt.value = 'Завершить продажу'

# progress bar
txt_progress_bar = ft.Text(value='',
                           font_family='Arial',
                           size=12,
                           color=ft.colors.WHITE70,
                           visible=False)

txt_progress_bar_order = copy.deepcopy(txt_progress_bar)
txt_progress_bar_order_sell = copy.deepcopy(txt_progress_bar)

# banner
banner_text = ft.Text("", color=ft.colors.RED)

# tools page
txt_progress_reset_password = ft.Text(value="", color=ft.colors.GREY)

# stands page
stands_text = ft.Text("", size=15, weight=ft.FontWeight.BOLD,
                      width=89, text_align=ft.TextAlign.CENTER)

stands_header = copy.deepcopy(stands_text)
stands_header.value = "Окружение Сервис"

stands_1 = copy.deepcopy(stands_text)
stands_1.value = "STAND 1"
stands_2 = copy.deepcopy(stands_text)
stands_2.value = "STAND 2"
stands_3 = copy.deepcopy(stands_text)
stands_3.value = "STAND 3"
stands_4 = copy.deepcopy(stands_text)
stands_4.value = "STAND 4"
stands_5 = copy.deepcopy(stands_text)
stands_5.value = "STAND 5"
stands_6 = copy.deepcopy(stands_text)
stands_6.value = "STAND 6"
stands_7 = copy.deepcopy(stands_text)
stands_7.value = "STAND 7"
stands_8 = copy.deepcopy(stands_text)
stands_8.value = "STAND 8"

# info page
container_app_version = ft.Text(
            value='Версия приложения: 1.0.0 \n',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

txt_tg = ft.Text(
            value='@KononovQA',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

txt_yt = ft.Text(
            value='@KononovQA',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

# autotests page
name_service = ft.Text(
        value='name_service',
        font_family='Arial',
        size=20,
        color=ft.colors.WHITE,
        offset=(0, -0.8))

example_horizontal_text = ft.Text(
        spans=[example_textspan],
        size=16,
        color=ft.colors.WHITE,
        rotate=ft.Rotate(angle=-1.57),
        offset=ft.Offset(0.025, 2.9)
    )
