import flet as ft

from components.button.styles import ButtonStyles
from components.text.text_span import TextSpans


class Texts:
    def __init__(self):
        # main text
        self.txt_main_text = ft.Text(value='',
                                     font_family='Arial',
                                     size=20,
                                     color=ft.colors.WHITE)

        self.txt_header_text = ft.Text(value='',
                                       style=ButtonStyles().header_text_style,
                                       color=ft.colors.WHITE,
                                       size=22)

        # text in buttons
        self.text_in_buttons = ft.Text(value='',
                                       text_align=ft.TextAlign.CENTER)

        # progress bar
        self.txt_progress_bar = ft.Text(value='',
                                        font_family='Arial',
                                        size=12,
                                        color=ft.colors.WHITE70,
                                        visible=False)

        # banner
        self.banner_text = ft.Text("",
                                   color=ft.colors.RED)

        # tools page
        self.txt_progress_reset_password = ft.Text(value="",
                                                   color=ft.colors.GREY)

        # stands page
        self.stands_text = ft.Text("",
                                   size=15,
                                   weight=ft.FontWeight.BOLD,
                                   width=89,
                                   text_align=ft.TextAlign.CENTER)

        # info page
        self.container_app_version = ft.Text(
            value='Версия приложения: 1.2.2 \n',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

        self.txt_creator_fio = ft.Text(
            value='Кононов Михаил Дмитриевич \n',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

        self.txt_tg = ft.Text(
            value='@KononovQA',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

        self.txt_yt = ft.Text(
            value='@KononovQA',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

        self.txt_github = ft.Text(
            value='@KononovQA',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

        self.txt_email = ft.Text(
            value='mk@kononovqa.ru',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

        self.txt_linkedin = ft.Text(
            value='михаил-к-2b4801233',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

        self.txt_inst = ft.Text(
            value='@yoshikitzu',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE)

        # autotests page
        self.name_service = ft.Text(
            value='name_service',
            font_family='Arial',
            size=20,
            color=ft.colors.WHITE,
            offset=(0, -0.8))

        self.example_horizontal_text = ft.Text(
            spans=[TextSpans().example_textspan],
            size=16,
            color=ft.colors.WHITE,
            rotate=ft.Rotate(angle=-1.57),
            offset=ft.Offset(0.025, 2.9)
        )

    def txt_header_main(self):
        self.txt_main_text.value = 'Главная'
        return self.txt_main_text

    def txt_header_tools(self):
        self.txt_main_text.value = 'Инструменты'
        return self.txt_main_text

    def txt_header_info(self):
        self.txt_main_text.value = 'Информация'
        return self.txt_main_text

    def txt_header_autotests(self):
        self.txt_main_text.value = 'Автотесты'
        return self.txt_main_text

    def txt_header_stands(self):
        self.txt_main_text.value = 'Стенды'
        return self.txt_main_text

    def txt_api_button(self):
        self.txt_main_text.value = 'API'
        return self.txt_main_text

    def txt_main_text_sell(self):
        self.txt_main_text.value = 'Создайте продажу'
        return self.txt_main_text

    def txt_main_text_order(self):
        self.txt_main_text.value = 'Создайте заказ'
        return self.txt_main_text

    def create_order_txt(self):
        self.text_in_buttons.value = 'Создать новый заказ'
        return self.text_in_buttons

    def button_product_txt(self):
        self.text_in_buttons.value = 'Выбрать поставщика и товар'
        return self.text_in_buttons

    def button_approve_txt(self):
        self.text_in_buttons.value = 'Согласовать'
        return self.text_in_buttons

    def button_deliver_txt(self):
        self.text_in_buttons.value = 'Доставить'
        return self.text_in_buttons

    def button_end_order_txt(self):
        self.text_in_buttons.value = 'Завершить заказ'
        return self.text_in_buttons

    def button_sell_txt(self):
        self.text_in_buttons.value = 'Создать продажу'
        return self.text_in_buttons

    def button_product_sell_txt(self):
        self.text_in_buttons.value = 'В работе'
        return self.text_in_buttons

    def button_add_product_txt(self):
        self.text_in_buttons.value = 'Добавить товары'
        return self.text_in_buttons

    def button_required_txt(self):
        self.text_in_buttons.value = 'Заполнить обязательные поля'
        return self.text_in_buttons

    def button_assign_driver_txt(self):
        self.text_in_buttons.value = 'Назначить водителя'
        return self.text_in_buttons

    def driver_in_storage_txt(self):
        self.text_in_buttons.value = 'Водитель на складе'
        return self.text_in_buttons

    def button_deliver_sell_txt(self):
        self.text_in_buttons.value = 'Доставка'
        return self.text_in_buttons

    def button_delivered_sell_txt(self):
        self.text_in_buttons.value = 'Доставлено'
        return self.text_in_buttons

    def button_end_order_assign_driver_txt(self):
        self.text_in_buttons.value = 'Заполнить документы'
        return self.text_in_buttons

    def button_end_sell_txt(self):
        self.text_in_buttons.value = 'Завершить продажу'
        return self.text_in_buttons

    def text_delete_order(self):
        self.text_in_buttons.value = "Удалить заказ"
        return self.text_in_buttons

    def text_button_reset_password(self):
        self.text_in_buttons.value = "Сбросить всем пользователям пароли"
        self.text_in_buttons.visible = False
        return self.text_in_buttons

    def stands_header(self):
        self.stands_text.value = "Окружение Сервис"
        return self.stands_text

    def stands_1(self):
        self.stands_text.value = "STAND 1"
        return self.stands_text

    def stands_2(self):
        self.stands_text.value = "STAND 2"
        return self.stands_text

    def stands_3(self):
        self.stands_text.value = "STAND 3"
        return self.stands_text

    def stands_4(self):
        self.stands_text.value = "STAND 4"
        return self.stands_text

    def stands_5(self):
        self.stands_text.value = "STAND 5"
        return self.stands_text

    def stands_6(self):
        self.stands_text.value = "STAND 6"
        return self.stands_text

    def stands_7(self):
        self.stands_text.value = "STAND 7"
        return self.stands_text

    def stands_8(self):
        self.stands_text.value = "STAND 8"
        return self.stands_text

    def dialog_order_txt(self):
        self.txt_header_text.value = "Выберите владельца заказа"
        return self.txt_header_text

    def dialog_sell_txt(self):
        self.txt_header_text.value = "Выберите владельца продажи"
        return self.txt_header_text
