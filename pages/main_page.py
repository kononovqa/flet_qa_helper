import random
import traceback
import flet as ft

from components.alert_dialog.alert_dialog import AlertDialogs
from components.button.elevated_button import ElevatedButtons
from components.button.icon_button import IconButtons
from components.button.styles import ButtonStyles
from components.container.container import Containers
from components.text.text import Texts
from components.text.text_field import TextFields
from components.progress_bar.progress_bar import ProgressBars

from autotest_requests.fake_do_something import do_something, do_something_failed
from data.variables import cst_head_list, list_users_sell


def main_page(page):
    button_order_container, button_order, button_settings = (
        Containers().button_order_container())
    button_product_container, button_product, button_repeat_product = (
        Containers().button_product_container())
    button_approve_container, button_approve, button_repeat_approve = (
        Containers().button_approve_container())
    button_deliver_container, button_deliver, button_repeat_deliver = (
        Containers().button_deliver_container())
    button_end_order_container, button_end_order, button_repeat_end_order = (
        Containers().button_end_order_container())

    button_sell_container, button_sell, button_settings_sell = (
        Containers().button_sell_container())
    button_in_work_sell_container, button_product_sell = (
        Containers().button_product_sell_container())
    button_add_product_container, button_add_product = (
        Containers().button_add_product_container())
    button_required_container, button_required, button_repeat_required = (
        Containers().button_required_container())
    button_assign_driver_container, button_assign_driver, button_repeat_assign_driver = (
        Containers().button_assign_driver_container())

    button_driver_in_storage_container, driver_in_storage = (
        Containers().button_driver_in_storage_container())
    button_deliver_sell_container, button_deliver_sell = (
        Containers().button_deliver_sell_container())
    button_delivered_sell_container, button_delivered_sell = (
        Containers().button_delivered_sell_container())
    button_sign_docs_container, button_end_order_assign_driver = (
        Containers().button_end_order_assign_driver_container())
    button_end_sell_container, button_end_sell = Containers().button_end_sell_container()

    dialog_order, dropdown_users_order = AlertDialogs().dialog_order()
    dialog_sell, dropdown_users_sell = AlertDialogs().dialog_sell()

    txt_progress_bar_order = Texts().txt_progress_bar
    txt_progress_bar_order_sell = Texts().txt_progress_bar
    banner_text = Texts().banner_text

    button_update = ElevatedButtons().button_update()
    button_push = ElevatedButtons().button_push()
    button_go_order = ElevatedButtons().button_go_to_link()
    button_copy_str_order = ElevatedButtons().button_copy()
    button_update_sell = ElevatedButtons().button_update()
    button_push_sell = ElevatedButtons().button_push()
    button_go_sell = ElevatedButtons().button_go_to_link()
    button_copy_str_sell = ElevatedButtons().button_copy()

    button_repeat_approve = IconButtons().button_icon_repeat_one

    container_txt_start_order, txt_main_text_order = (
        Containers().container_txt_start_order())
    container_txt_start_sell, txt_main_text_sell = (
        Containers().container_txt_start_sell())

    button_empty = Containers().button_empty_sample
    button_empty_2 = Containers().button_empty_sample

    txt_go_order = TextFields().txt_go_order()
    txt_creator_order = TextFields().txt_creator_order()
    txt_go_sell = TextFields().txt_go_sell()
    txt_sell_str = TextFields().txt_sell_str()

    progress_bar_order = ProgressBars().progress_bar
    progress_bar_sell = ProgressBars().progress_bar

    row_order = ft.Row([button_order_container,
                        button_product_container,
                        button_approve_container,
                        button_deliver_container,
                        button_end_order_container,
                        button_update,
                        button_push],
                       alignment=ft.MainAxisAlignment.CENTER,
                       vertical_alignment=ft.CrossAxisAlignment.CENTER,
                       offset=(0, -0.17))

    row_txt_progress_bar_order = ft.Row([txt_progress_bar_order],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        offset=(0, -0.5))

    row_progress_bar_order = ft.Row([progress_bar_order],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    offset=(0, -0.6))

    row_go_order = ft.Row([txt_go_order, button_go_order],
                          alignment=ft.MainAxisAlignment.CENTER,
                          vertical_alignment=ft.CrossAxisAlignment.CENTER,
                          height=65,
                          visible=False)

    row_creator_order = ft.Row([txt_creator_order, button_copy_str_order],
                               alignment=ft.MainAxisAlignment.CENTER,
                               vertical_alignment=ft.CrossAxisAlignment.CENTER,
                               height=65,
                               visible=False)

    row_sell_first = ft.Row([button_sell_container,
                             button_in_work_sell_container,
                             button_add_product_container,
                             button_required_container,
                             button_assign_driver_container,
                             button_empty,
                             button_empty_2],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            offset=(0, -0.25))

    row_sell_second = ft.Row([button_driver_in_storage_container,
                              button_deliver_sell_container,
                              button_delivered_sell_container,
                              button_sign_docs_container,
                              button_end_sell_container,
                              button_update_sell,
                              button_push_sell],
                             alignment=ft.MainAxisAlignment.CENTER,
                             vertical_alignment=ft.CrossAxisAlignment.CENTER,
                             offset=(0, -0.25))

    row_txt_progress_bar_sell = ft.Row([txt_progress_bar_order_sell],
                                       alignment=ft.MainAxisAlignment.CENTER,
                                       vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                       offset=(0, -0.5))

    row_progress_bar_sell = ft.Row([progress_bar_sell],
                                   alignment=ft.MainAxisAlignment.CENTER,
                                   vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                   offset=(0, -0.6))

    row_go_sell = ft.Row([txt_go_sell, button_go_sell],
                         alignment=ft.MainAxisAlignment.CENTER,
                         vertical_alignment=ft.CrossAxisAlignment.CENTER,
                         height=65,
                         visible=False)

    row_sell_str = ft.Row([txt_sell_str, button_copy_str_sell],
                          alignment=ft.MainAxisAlignment.CENTER,
                          vertical_alignment=ft.CrossAxisAlignment.CENTER,
                          height=65,
                          visible=False)

    def resize():
        width_page = int(page.width)
        if width_page < 1330:
            row_order.scroll = ft.ScrollMode.ADAPTIVE
            row_go_order.scroll = ft.ScrollMode.ADAPTIVE
            txt_go_order.width = width_page - 110
            row_creator_order.scroll = ft.ScrollMode.ADAPTIVE
            txt_creator_order.width = width_page - 110
            row_sell_first.scroll = ft.ScrollMode.ADAPTIVE
            row_sell_second.scroll = ft.ScrollMode.ADAPTIVE
            row_go_sell.scroll = ft.ScrollMode.ADAPTIVE
            txt_go_sell.width = width_page - 110
            row_sell_str.scroll = ft.ScrollMode.ADAPTIVE
            txt_sell_str.width = width_page - 110
            progress_bar_order.width = width_page - 30
            progress_bar_sell.width = width_page - 30

        else:
            row_order.scroll = False
            row_go_order.scroll = False
            txt_go_order.width = 1230
            row_creator_order.scroll = False
            txt_creator_order.width = 1230
            row_sell_first.scroll = False
            row_sell_second.scroll = False
            row_go_sell.scroll = False
            txt_go_sell.width = 1230
            row_sell_str.scroll = False
            txt_sell_str.width = 1230
            progress_bar_order.width = 1310
            progress_bar_sell.width = 1310

        if width_page < 930:
            width_button = 140
        elif 930 < width_page <= 1330:
            width_button = (width_page - 172 - 57) / 5
        else:
            width_button = 220

        button_order_container.width = width_button
        button_product_container.width = width_button
        button_approve_container.width = width_button
        button_deliver_container.width = width_button
        button_end_order_container.width = width_button

        button_sell_container.width = width_button
        button_in_work_sell_container.width = width_button
        button_add_product_container.width = width_button
        button_required_container.width = width_button
        button_assign_driver_container.width = width_button

        button_driver_in_storage_container.width = width_button
        button_deliver_sell_container.width = width_button
        button_delivered_sell_container.width = width_button
        button_sign_docs_container.width = width_button
        button_end_sell_container.width = width_button

    resize()

    async def page_resize(e):
        resize()
        await page.update_async()

    page.on_resize = page_resize

    async def button_pressed(button_main, button_side, progress_bar,
                             progress_bar_text_field, text_above_pb, page):
        button_main.disabled = True
        button_main.style = ButtonStyles().button_style_pressed_wait
        button_side.disabled = True
        button_side.style = ButtonStyles().button_style_disabled
        button_side.icon_color = ft.colors.GREY
        progress_bar.visible = True
        progress_bar.value = 0.01
        progress_bar.color = ft.colors.GREEN
        progress_bar_text_field.visible = True
        progress_bar_text_field.value = text_above_pb

        await page.update_async()

    async def button_failed(button_main, button_side, progress_bar, button_update, page,
                            is_button_settings=False):
        button_main.disabled = True
        button_main.style = ButtonStyles().button_style_failed_disabled
        if is_button_settings:
            button_side.disabled = True
            button_side.icon_color = ft.colors.RED
        else:
            button_side.disabled = False
            button_side.style = ButtonStyles().button_style_enabled
            button_side.icon_color = ft.colors.CYAN

        progress_bar.color = ft.colors.RED
        button_update.disabled = False
        button_update.style = ButtonStyles().button_style_enabled
        await page.update_async()

    async def button_success(button_main, button_side, page, is_settings_button=False):
        button_main.disabled = True
        button_main.style = ButtonStyles().button_style_pressed_access

        button_side.disabled = True
        if is_settings_button:
            button_side.icon_color = ft.colors.GREEN
        else:
            button_side.icon_color = ft.colors.GREY
        await page.update_async()

    async def press_create_order(e):
        await button_pressed(button_order, button_settings, progress_bar_order,
                             txt_progress_bar_order, 'Запускаем процесс', page)

        button_push.disabled = True
        button_push.style = ButtonStyles().button_style_disabled

        await page.update_async()

        try:
            user_for_create = dropdown_users_order.value
            if user_for_create is None or user_for_create == 'Случайный':
                user_for_create = random.choice(cst_head_list)
            await change_progress_bar(progress_bar_order, 0.3)

            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Создаём заказ', page)
            await do_something()
            await change_progress_bar(progress_bar_order, 0.4)
            url_project_order = f'https://www.google.ru/search?q={user_for_create}'
            txt_go_order.value = url_project_order
            txt_go_order.visible = True
            row_go_order.visible = True
            row_creator_order.visible = True
            button_go_order.visible = True
            txt_creator_order.value = user_for_create
            txt_creator_order.visible = True
            button_copy_str_order.visible = True
            await page.update_async()

            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Инициируем', page)
            await do_something()
            await change_progress_bar(progress_bar_order, 1)

            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Успешно', page)

            button_update.disabled = False
            button_update.style = ButtonStyles().button_style_enabled

            await page.update_async()
        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(button_order, button_settings, progress_bar_order,
                                button_update, page, is_button_settings=True)
            return 0

        button_approve.disabled = False
        button_approve.style = ButtonStyles().button_style_enabled
        button_product.disabled = False
        button_product.style = ButtonStyles().button_style_enabled

        button_deliver.disabled = False
        button_deliver.style = ButtonStyles().button_style_enabled

        txt_main_text_order.value = 'Завершите заказ'
        container_txt_start_order.content = txt_main_text_order
        await button_success(button_order, button_settings, page, True)

    async def press_product(e):
        await button_pressed(button_product, button_repeat_product, progress_bar_order,
                             txt_progress_bar_order, 'Запускаем процесс', page)
        await page.update_async()

        try:
            await do_something()
            await change_progress_bar(progress_bar_order, 1)
            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Успешно', page)
        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(button_product, button_repeat_product, progress_bar_order,
                                button_update, page)
            return 0

        if button_deliver.style.color == 'green':
            button_end_order.disabled = False
            button_end_order.style = ButtonStyles().button_style_enabled
        await button_success(button_product, button_repeat_product, page)

    async def press_approve(e):
        await button_pressed(button_approve, button_repeat_approve, progress_bar_order,
                             txt_progress_bar_order, 'Запускаем процесс', page)
        await page.update_async()

        try:
            await do_something()
            await change_progress_bar(progress_bar_order, 1)
            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Успешно', page)
        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(button_approve, button_repeat_approve, progress_bar_order,
                                button_update, page)
            return 0

        await button_success(button_approve, button_repeat_approve, page)

    async def press_deliver(e):
        await button_pressed(button_deliver, button_repeat_deliver, progress_bar_order,
                             txt_progress_bar_order, 'Запускаем процесс', page)
        await page.update_async()

        try:
            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Доставляем', page)
            await do_something()
            await change_progress_bar(progress_bar_order, 1)

            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Успешно', page)

        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(button_deliver, button_repeat_deliver, progress_bar_order,
                                button_update, page)
            return 0

        if button_product.style.color == 'green':
            button_end_order.disabled = False
            button_end_order.style = ButtonStyles().button_style_enabled
        await button_success(button_deliver, button_repeat_deliver, page)

    async def press_end_order(e):
        await button_pressed(button_end_order, button_repeat_end_order,
                             progress_bar_order,
                             txt_progress_bar_order, 'Запускаем процесс', page)
        await page.update_async()

        try:
            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Завершаем заказ', page)
            await do_something()
            await change_progress_bar(progress_bar_order, 1)

            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Успешно', page)

        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(button_end_order, button_repeat_end_order,
                                progress_bar_order,
                                button_update, page)
            return 0

        await button_success(button_end_order, button_repeat_end_order, page)

    async def press_update(e):
        txt_main_text_order.value = 'Создайте заказ'
        container_txt_start_order.content = txt_main_text_order

        progress_bar_order.value = 0
        progress_bar_order.visible = False
        txt_progress_bar_order.visible = False

        button_update.style = ButtonStyles().button_style_disabled
        button_update.disabled = True

        button_order.disabled = False
        button_order.style = ButtonStyles().button_style_enabled

        button_product.disabled = True
        button_product.style = ButtonStyles().button_style_disabled

        button_approve.disabled = True
        button_approve.style = ButtonStyles().button_style_disabled

        button_deliver.disabled = True
        button_deliver.style = ButtonStyles().button_style_disabled

        button_end_order.disabled = True
        button_end_order.style = ButtonStyles().button_style_disabled

        button_push.disabled = False
        button_push.style = ButtonStyles().button_style_enabled

        txt_go_order.visible = False
        button_go_order.visible = False
        row_go_order.visible = False
        row_creator_order.visible = False

        txt_creator_order.visible = False
        button_copy_str_order.visible = False

        button_repeat_approve.disabled = True
        button_repeat_product.disabled = True
        button_repeat_deliver.disabled = True
        button_repeat_end_order.disabled = True

        button_repeat_approve.style = ButtonStyles().button_style_disabled
        button_repeat_product.style = ButtonStyles().button_style_disabled
        button_repeat_deliver.style = ButtonStyles().button_style_disabled
        button_repeat_end_order.style = ButtonStyles().button_style_disabled

        button_repeat_approve.icon_color = ft.colors.GREY
        button_repeat_product.icon_color = ft.colors.GREY
        button_repeat_deliver.icon_color = ft.colors.GREY
        button_repeat_end_order.icon_color = ft.colors.GREY

        button_settings.disabled = False
        button_settings.icon_color = ft.colors.CYAN

        await page.update_async()

    async def press_update_sell(e):
        txt_main_text_sell.value = 'Создайте продажу'
        container_txt_start_sell.content = txt_main_text_sell

        progress_bar_sell.value = 0
        progress_bar_sell.visible = False
        txt_progress_bar_order_sell.visible = False

        button_update_sell.style = ButtonStyles().button_style_disabled
        button_update_sell.disabled = True

        button_sell.style = ButtonStyles().button_style_enabled
        button_sell.disabled = False

        button_required.style = ButtonStyles().button_style_disabled
        button_required.disabled = True

        button_assign_driver.style = ButtonStyles().button_style_disabled
        button_assign_driver.disabled = True

        txt_go_sell.visible = False
        button_go_sell.visible = False
        row_go_sell.visible = True
        row_sell_str.visible = True

        txt_sell_str.visible = False
        button_copy_str_sell.visible = False

        button_push_sell.disabled = False
        button_push_sell.style = ButtonStyles().button_style_enabled

        button_repeat_required.disabled = True
        button_repeat_assign_driver.disabled = True

        button_repeat_required.style = ButtonStyles().button_style_disabled
        button_repeat_assign_driver.style = ButtonStyles().button_style_disabled

        button_repeat_required.icon_color = ft.colors.GREY
        button_repeat_assign_driver.icon_color = ft.colors.GREY

        button_settings_sell.disabled = False
        button_settings_sell.icon_color = ft.colors.CYAN

        await page.update_async()

    async def press_sell(e):
        button_push_sell.disabled = True
        button_push_sell.style = ButtonStyles().button_style_disabled

        await button_pressed(button_sell, button_settings_sell, progress_bar_sell,
                             txt_progress_bar_order_sell, 'Запускаем процесс', page)

        try:
            txt_main_text_sell.value = 'Завершите продажу'
            container_txt_start_sell.content = txt_main_text_sell
            await page.update_async()

            user_for_create = dropdown_users_sell.value
            if user_for_create is None or user_for_create == 'Случайный':
                user_for_create = random.choice(list_users_sell)
            await change_progress_bar(progress_bar_sell, 0.3)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Создаем продажу', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.5)

            url_sell = f'https://www.google.ru/search?q={user_for_create}'
            txt_go_sell.value = url_sell
            txt_go_sell.visible = True
            button_go_sell.visible = True
            row_go_sell.visible = True
            row_sell_str.visible = True
            txt_sell_str.value = user_for_create
            txt_sell_str.visible = True
            button_copy_str_sell.visible = True

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Устанавливаем дату старта', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.6)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Устанавливаем дату окончания', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.7)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Устанавливаем владельца', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.8)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Устанавливаем отдел', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.9)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Устанавливаем ответственного', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.95)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Инициируем продажу', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 1)

            button_update_sell.disabled = False
            button_update_sell.style = ButtonStyles().button_style_enabled

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Успешно', page)

        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(button_sell, button_settings_sell, progress_bar_sell,
                                button_update_sell, page, is_button_settings=True)
            return 0

        button_required.disabled = False
        button_required.style = ButtonStyles().button_style_enabled
        button_assign_driver.disabled = False
        button_assign_driver.style = ButtonStyles().button_style_enabled
        await button_success(button_sell, button_settings_sell, page, True)

    async def press_push(e):
        if await press_create_order(e) != 0:
            if await press_product(e) != 0:
                if await press_approve(e) != 0:
                    if await press_deliver(e) != 0:
                        await press_end_order(e)

    async def press_push_sell(e):
        if await press_sell(e) != 0:
            if await press_required(e) != 0:
                await press_assign_driver(e)

    async def press_required(e):
        await button_pressed(button_required, button_repeat_required, progress_bar_sell,
                             txt_progress_bar_order_sell, 'Запускаем процесс', page)
        try:
            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Авторизуемся за пользователя', page)
            await do_something_failed()
            await change_progress_bar(progress_bar_sell, 0.2)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Заполняем точку доставки', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.6)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Выбираем контрагента',
                                          page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.75)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Переводим продажу в статус "Заполнено"',
                                          page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 1)
            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Успешно', page)

        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(button_required, button_repeat_required,
                                progress_bar_sell,
                                button_update_sell, page)
            return 0

        await button_success(button_required, button_repeat_required, page, True)

    async def press_assign_driver(e):
        await button_pressed(button_assign_driver, button_repeat_assign_driver,
                             progress_bar_sell, txt_progress_bar_order_sell,
                             'Запускаем процесс', page)
        try:
            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Авторизуемся за пользователя', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.2)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Запрашиваем список водителей', page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.6)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Выбираем водителя',
                                          page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.75)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Завершено',
                                          page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 1)

        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(button_assign_driver, button_repeat_assign_driver,
                                progress_bar_sell, button_update_sell, page)
            return 0

        await button_success(button_assign_driver, button_repeat_assign_driver, page,
                             True)

    async def press_go_order(e):
        await page.launch_url_async(txt_go_order.value)

    async def press_go_sell(e):
        await page.launch_url_async(txt_go_sell.value)

    async def press_dialog_order(e):
        button_settings.disabled = True
        button_settings.icon_color = ft.colors.GREY
        await page.update_async()

        page.dialog = dialog_order
        dialog_order.open = True

        try:
            await do_something()
        except:
            await open_banner_with_error(traceback.format_exc())
            return 0

        dropdown_users_order.options.clear()
        dropdown_users_order.options.append(ft.dropdown.Option('Случайный'))
        for user in cst_head_list:
            dropdown_users_order.options.append(ft.dropdown.Option(user))
        await page.update_async()

    async def press_dialog_sell(e):
        button_settings_sell.disabled = True
        button_settings_sell.icon_color = ft.colors.GREY
        await page.update_async()

        page.dialog = dialog_sell
        dialog_sell.open = True
        try:
            await do_something()
        except:
            await open_banner_with_error(traceback.format_exc())
            button_settings_sell.disabled = False
            button_settings_sell.icon_color = ft.colors.RED
            await page.update_async()
            traceback.print_exc()
            return 0

        dropdown_users_sell.options.clear()
        dropdown_users_sell.options.append(ft.dropdown.Option('Случайный'))
        for user in list_users_sell:
            dropdown_users_sell.options.append(ft.dropdown.Option(user))
        await page.update_async()

    async def switch_txt_progress_bar(txt_field, txt_to_switch, page):
        txt_field.value = txt_to_switch
        await page.update_async()

    async def close_banner(e):
        page.banner.open = False
        await page.update_async()

    async def open_banner_with_error(error_text):
        page.banner.open = True
        banner_text.value = (f'Ошибка: '
                             f'\n {error_text}')
        await page.update_async()
        traceback.print_exc()

    async def change_progress_bar(progress_bar_name, new_value):
        progress_bar_name.value = new_value
        await page.update_async()

    async def copy_in_buffer_txt_order(e):
        await page.set_clipboard_async(txt_creator_order.value)

    async def copy_in_buffer_txt_sell(e):
        await page.set_clipboard_async(txt_sell_str.value)

    async def copy_in_buffer_txt_banner(e):
        await page.set_clipboard_async(banner_text.value)

    async def dialog_exit(e):
        dialog_order.open = False
        dialog_sell.open = False
        if button_settings.disabled and button_settings.icon_color != 'green':
            button_settings.disabled = False
            button_settings.icon_color = ft.colors.CYAN
        elif button_settings_sell.disabled and button_settings_sell.icon_color != 'green':
            button_settings_sell.disabled = False
            button_settings_sell.icon_color = ft.colors.CYAN
        await page.update_async()

    button_repeat_required.on_click = press_required
    button_repeat_assign_driver.on_click = press_assign_driver
    button_repeat_product.on_click = press_product
    button_repeat_approve.on_click = press_approve
    button_repeat_deliver.on_click = press_deliver
    button_repeat_end_order.on_click = press_end_order

    button_settings.on_click = press_dialog_order
    button_settings_sell.on_click = press_dialog_sell

    dialog_order.on_dismiss = dialog_exit
    dialog_sell.on_dismiss = dialog_exit

    button_order.on_click = press_create_order
    button_product.on_click = press_product
    button_approve.on_click = press_approve
    button_deliver.on_click = press_deliver
    button_end_order.on_click = press_end_order
    button_update.on_click = press_update
    button_push.on_click = press_push

    button_go_order.on_click = press_go_order
    button_copy_str_order.on_click = copy_in_buffer_txt_order

    button_sell.on_click = press_sell
    button_required.on_click = press_required
    button_assign_driver.on_click = press_assign_driver

    button_update_sell.on_click = press_update_sell
    button_push_sell.on_click = press_push_sell

    button_go_sell.on_click = press_go_sell
    button_copy_str_sell.on_click = copy_in_buffer_txt_sell

    page.banner = ft.Banner(
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.RED, size=40),
        content=ft.Column([banner_text], width=1400, height=250,
                          scroll=ft.ScrollMode.ALWAYS),
        actions=[
            ft.IconButton(icon=ft.icons.COPY,
                          icon_color=ft.colors.CYAN,
                          on_click=copy_in_buffer_txt_banner),
            ft.IconButton(icon=ft.icons.CLOSE,
                          icon_color=ft.colors.CYAN,
                          on_click=close_banner),
        ],
    )

    content = ft.Column([
        container_txt_start_order,
        row_order,
        row_txt_progress_bar_order,
        row_progress_bar_order,
        row_go_order,
        row_creator_order,
        container_txt_start_sell,
        row_sell_first,
        row_sell_second,
        row_txt_progress_bar_sell,
        row_progress_bar_sell,
        row_go_sell,
        row_sell_str
    ])

    return content
