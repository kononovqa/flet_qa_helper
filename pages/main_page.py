import random
import traceback
import flet as ft

from components.alert_dialog.alert_dialog import dlg_order, dlg_sell
from components.button.elevated_button import bttn_order, bttn_product, bttn_approve,  \
    bttn_end_order, bttn_update, bttn_push, bttn_go_order, bttn_copy_str_order, \
    bttn_required, bttn_assign_driver, bttn_update_sell, bttn_push_sell, bttn_go_sell, \
    bttn_copy_str_sell, bttn_deliver, bttn_sell
from components.button.icon_button import bttn_repeat_required, \
    bttn_repeat_assign_driver, bttn_repeat_product, bttn_repeat_approve, \
    bttn_settings_sell, bttn_repeat_end_order, bttn_repeat_deliver, bttn_settings
from components.button.styles import button_style_pressed_wait, button_style_disabled, \
    button_style_enabled, button_style_failed_disabled, button_style_pressed_access
from components.container.container import container_txt_start_order, \
    container_txt_start_sell, bttn_order_container, bttn_product_container, \
    bttn_deliver_container, bttn_end_order_container, bttn_sell_container, \
    bttn_add_product_container, bttn_required_container, bttn_assign_driver_container, \
    bttn_driver_in_storage_container, bttn_deliver_sell_container, \
    bttn_sign_docs_container, bttn_end_sell_container, bttn_empty, bttn_empty_2, \
    bttn_in_work_sell_container, bttn_approve_container, bttn_delivered_sell_container
from components.dropdown.dropdown import dropdown_users_sell, dropdown_users_order
from components.text.text import txt_progress_bar_order, txt_progress_bar_order_sell, \
    banner_text, txt_main_text_order, txt_main_text_sell
from components.text_field.text_field import txt_go_order, txt_creator_order, \
    txt_go_sell, txt_sell_str
from components.progress_bar.progress_bar import (
    progress_bar_order, progress_bar_sell)

from press_button.fake_do_something import do_something, do_something_failed
from data.variables import cst_head_list, list_users_sell


def main_page(page):
    async def button_pressed(button_main, button_side, progress_bar,
                             progress_bar_text_field, text_above_pb, page):
        button_main.disabled = True
        button_main.style = button_style_pressed_wait
        button_side.disabled = True
        button_side.style = button_style_disabled
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
        button_main.style = button_style_failed_disabled
        if is_button_settings:
            button_side.disabled = True
            button_side.icon_color = ft.colors.RED
        else:
            button_side.disabled = False
            button_side.style = button_style_enabled
            button_side.icon_color = ft.colors.CYAN

        progress_bar.color = ft.colors.RED
        button_update.disabled = False
        button_update.style = button_style_enabled
        await page.update_async()

    async def button_success(button_main, button_side, page, is_settings_button=False):
        button_main.disabled = True
        button_main.style = button_style_pressed_access

        button_side.disabled = True
        if is_settings_button:
            button_side.icon_color = ft.colors.GREEN
        else:
            button_side.icon_color = ft.colors.GREY
        await page.update_async()

    async def press_create_order(e):
        await button_pressed(bttn_order, bttn_settings, progress_bar_order,
                             txt_progress_bar_order, 'Запускаем процесс', page)

        bttn_push.disabled = True
        bttn_push.style = button_style_disabled

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
            bttn_go_order.visible = True
            txt_creator_order.value = user_for_create
            txt_creator_order.visible = True
            bttn_copy_str_order.visible = True
            await page.update_async()

            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Инициируем', page)
            await do_something()
            await change_progress_bar(progress_bar_order, 1)

            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Успешно', page)

            bttn_update.disabled = False
            bttn_update.style = button_style_enabled

            await page.update_async()
        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(bttn_order, bttn_settings, progress_bar_order,
                                bttn_update, page, is_button_settings=True)
            return 0

        bttn_approve.disabled = False
        bttn_approve.style = button_style_enabled
        bttn_product.disabled = False
        bttn_product.style = button_style_enabled

        bttn_deliver.disabled = False
        bttn_deliver.style = button_style_enabled

        txt_main_text_order.value = 'Завершите заказ'
        container_txt_start_order.content = txt_main_text_order
        await button_success(bttn_order, bttn_settings, page, True)

    async def press_product(e):
        await button_pressed(bttn_product, bttn_repeat_product, progress_bar_order,
                             txt_progress_bar_order, 'Запускаем процесс', page)
        await page.update_async()

        try:
            await do_something()
            await change_progress_bar(progress_bar_order, 1)
            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Успешно', page)
        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(bttn_product, bttn_repeat_product, progress_bar_order,
                                bttn_update, page)
            return 0

        if bttn_deliver.style.color == 'green':
            bttn_end_order.disabled = False
            bttn_end_order.style = button_style_enabled
        await button_success(bttn_product, bttn_repeat_product, page)

    async def press_approve(e):
        await button_pressed(bttn_approve, bttn_repeat_approve, progress_bar_order,
                             txt_progress_bar_order, 'Запускаем процесс', page)
        await page.update_async()

        try:
            await do_something()
            await change_progress_bar(progress_bar_order, 1)
            await switch_txt_progress_bar(txt_progress_bar_order,
                                          'Успешно', page)
        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(bttn_approve, bttn_repeat_approve, progress_bar_order,
                                bttn_update, page)
            return 0

        await button_success(bttn_approve, bttn_repeat_approve, page)

    async def press_deliver(e):
        await button_pressed(bttn_deliver, bttn_repeat_deliver, progress_bar_order,
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
            await button_failed(bttn_deliver, bttn_repeat_deliver, progress_bar_order,
                                bttn_update, page)
            return 0

        if bttn_product.style.color == 'green':
            bttn_end_order.disabled = False
            bttn_end_order.style = button_style_enabled
        await button_success(bttn_deliver, bttn_repeat_deliver, page)

    async def press_end_order(e):
        await button_pressed(bttn_end_order, bttn_repeat_end_order, progress_bar_order,
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
            await button_failed(bttn_end_order, bttn_repeat_end_order, progress_bar_order,
                                bttn_update, page)
            return 0

        await button_success(bttn_end_order, bttn_repeat_end_order, page)

    async def press_update(e):
        txt_main_text_order.value = 'Создайте заказ'
        container_txt_start_order.content = txt_main_text_order

        progress_bar_order.value = 0
        progress_bar_order.visible = False
        txt_progress_bar_order.visible = False

        bttn_update.style = button_style_disabled
        bttn_update.disabled = True

        bttn_order.disabled = False
        bttn_order.style = button_style_enabled

        bttn_product.disabled = True
        bttn_product.style = button_style_disabled

        bttn_approve.disabled = True
        bttn_approve.style = button_style_disabled

        bttn_deliver.disabled = True
        bttn_deliver.style = button_style_disabled

        bttn_end_order.disabled = True
        bttn_end_order.style = button_style_disabled

        bttn_push.disabled = False
        bttn_push.style = button_style_enabled

        txt_go_order.visible = False
        bttn_go_order.visible = False

        txt_creator_order.visible = False
        bttn_copy_str_order.visible = False

        bttn_repeat_approve.disabled = True
        bttn_repeat_product.disabled = True
        bttn_repeat_deliver.disabled = True
        bttn_repeat_end_order.disabled = True

        bttn_repeat_approve.style = button_style_disabled
        bttn_repeat_product.style = button_style_disabled
        bttn_repeat_deliver.style = button_style_disabled
        bttn_repeat_end_order.style = button_style_disabled

        bttn_repeat_approve.icon_color = ft.colors.GREY
        bttn_repeat_product.icon_color = ft.colors.GREY
        bttn_repeat_deliver.icon_color = ft.colors.GREY
        bttn_repeat_end_order.icon_color = ft.colors.GREY

        bttn_settings.disabled = False
        bttn_settings.icon_color = ft.colors.CYAN

        await page.update_async()

    async def press_update_sell(e):
        txt_main_text_sell.value = 'Создайте продажу'
        container_txt_start_sell.content = txt_main_text_sell

        progress_bar_sell.value = 0
        progress_bar_sell.visible = False
        txt_progress_bar_order_sell.visible = False

        bttn_update_sell.style = button_style_disabled
        bttn_update_sell.disabled = True

        bttn_sell.style = button_style_enabled
        bttn_sell.disabled = False

        bttn_required.style = button_style_disabled
        bttn_required.disabled = True

        bttn_assign_driver.style = button_style_disabled
        bttn_assign_driver.disabled = True

        txt_go_sell.visible = False
        bttn_go_sell.visible = False

        txt_sell_str.visible = False
        bttn_copy_str_sell.visible = False

        bttn_push_sell.disabled = False
        bttn_push_sell.style = button_style_enabled

        bttn_repeat_required.disabled = True
        bttn_repeat_assign_driver.disabled = True

        bttn_repeat_required.style = button_style_disabled
        bttn_repeat_assign_driver.style = button_style_disabled

        bttn_repeat_required.icon_color = ft.colors.GREY
        bttn_repeat_assign_driver.icon_color = ft.colors.GREY

        bttn_settings_sell.disabled = False
        bttn_settings_sell.icon_color = ft.colors.CYAN

        await page.update_async()

    async def press_sell(e):
        bttn_push_sell.disabled = True
        bttn_push_sell.style = button_style_disabled

        await button_pressed(bttn_sell, bttn_settings_sell, progress_bar_sell,
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
            bttn_go_sell.visible = True
            txt_sell_str.value = user_for_create
            txt_sell_str.visible = True
            bttn_copy_str_sell.visible = True

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

            bttn_update_sell.disabled = False
            bttn_update_sell.style = button_style_enabled

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Успешно', page)

        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(bttn_sell, bttn_settings_sell, progress_bar_sell,
                                bttn_update_sell, page, is_button_settings=True)
            return 0

        bttn_required.disabled = False
        bttn_required.style = button_style_enabled
        bttn_assign_driver.disabled = False
        bttn_assign_driver.style = button_style_enabled
        await button_success(bttn_sell, bttn_settings_sell, page, True)

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
        await button_pressed(bttn_required, bttn_repeat_required, progress_bar_sell,
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
            await button_failed(bttn_required, bttn_repeat_required, progress_bar_sell,
                                bttn_update_sell, page)
            return 0

        await button_success(bttn_required, bttn_repeat_required, page, True)

    async def press_assign_driver(e):
        await button_pressed(bttn_assign_driver, bttn_repeat_assign_driver,
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
                                          'Сортируем по доступным для выбора',
                                          page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 0.75)

            await switch_txt_progress_bar(txt_progress_bar_order_sell,
                                          'Выбираем водителя',
                                          page)
            await do_something()
            await change_progress_bar(progress_bar_sell, 1)

        except:
            await open_banner_with_error(traceback.format_exc())
            await button_failed(bttn_assign_driver, bttn_repeat_assign_driver,
                                progress_bar_sell, bttn_update_sell, page)
            return 0

        await button_success(bttn_assign_driver, bttn_repeat_assign_driver, page, True)

    async def press_go_order(e):
        await page.launch_url_async(txt_go_order.value)

    async def press_go_sell(e):
        await page.launch_url_async(txt_go_sell.value)

    async def press_dlg_order(e):
        bttn_settings.disabled = True
        bttn_settings.icon_color = ft.colors.GREY
        await page.update_async()

        page.dialog = dlg_order
        dlg_order.open = True

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

    async def press_dlg_sell(e):
        bttn_settings_sell.disabled = True
        bttn_settings_sell.icon_color = ft.colors.GREY
        await page.update_async()

        page.dialog = dlg_sell
        dlg_sell.open = True
        try:
            await do_something()
        except:
            await open_banner_with_error(traceback.format_exc())
            bttn_settings_sell.disabled = False
            bttn_settings_sell.icon_color = ft.colors.RED
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

    async def dlg_exit(e):
        if bttn_settings.disabled:
            bttn_settings.disabled = False
            bttn_settings.icon_color = ft.colors.CYAN
        elif bttn_settings_sell.disabled:
            bttn_settings_sell.disabled = False
            bttn_settings_sell.icon_color = ft.colors.CYAN
        await page.update_async()

    bttn_repeat_required.on_click = press_required
    bttn_repeat_assign_driver.on_click = press_assign_driver
    bttn_repeat_product.on_click = press_product
    bttn_repeat_approve.on_click = press_approve
    bttn_repeat_deliver.on_click = press_deliver
    bttn_repeat_end_order.on_click = press_end_order

    bttn_settings.on_click = press_dlg_order
    bttn_settings_sell.on_click = press_dlg_sell

    dlg_order.on_dismiss = dlg_exit
    dlg_sell.on_dismiss = dlg_exit

    bttn_order.on_click = press_create_order
    bttn_product.on_click = press_product
    bttn_approve.on_click = press_approve
    bttn_deliver.on_click = press_deliver
    bttn_end_order.on_click = press_end_order
    bttn_update.on_click = press_update
    bttn_push.on_click = press_push

    bttn_go_order.on_click = press_go_order
    bttn_copy_str_order.on_click = copy_in_buffer_txt_order

    bttn_sell.on_click = press_sell
    bttn_required.on_click = press_required
    bttn_assign_driver.on_click = press_assign_driver

    bttn_update_sell.on_click = press_update_sell
    bttn_push_sell.on_click = press_push_sell

    bttn_go_sell.on_click = press_go_sell
    bttn_copy_str_sell.on_click = copy_in_buffer_txt_sell

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
        ft.Row([bttn_order_container,
                bttn_product_container,
                bttn_approve_container,
                bttn_deliver_container,
                bttn_end_order_container,
                bttn_update,
                bttn_push],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, -0.17)),
        ft.Row([txt_progress_bar_order],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, -0.5)),
        ft.Row([progress_bar_order],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, -0.6)),
        ft.Row([txt_go_order, bttn_go_order],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER),
        ft.Row([txt_creator_order, bttn_copy_str_order],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER),
        container_txt_start_sell,
        ft.Row([bttn_sell_container,
                bttn_in_work_sell_container,
                bttn_add_product_container,
                bttn_required_container,
                bttn_assign_driver_container,
                bttn_empty,
                bttn_empty_2],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, -0.25)),
        ft.Row([bttn_driver_in_storage_container,
                bttn_deliver_sell_container,
                bttn_delivered_sell_container,
                bttn_sign_docs_container,
                bttn_end_sell_container,
                bttn_update_sell,
                bttn_push_sell],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, -0.25)),
        ft.Row([txt_progress_bar_order_sell],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, -0.5)),
        ft.Row([progress_bar_sell],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               offset=(0, -0.6)),
        ft.Row([txt_go_sell, bttn_go_sell],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER),
        ft.Row([txt_sell_str, bttn_copy_str_sell],
               alignment=ft.MainAxisAlignment.CENTER,
               vertical_alignment=ft.CrossAxisAlignment.CENTER),
    ])

    return content
