import flet as ft


class Icons:
    def __init__(self):
        self.icon_rotate_right = ft.Icon(name=ft.icons.ROTATE_RIGHT)

        self.icon_push = ft.Icon(name=ft.icons.FAST_FORWARD)

        self.icon_send = ft.Icon(name=ft.icons.SEND)

        self.icon_copy = ft.Icon(name=ft.icons.COPY)

        self.icon_delete = ft.Icon(name=ft.icons.DELETE)

        self.icon_lock = ft.icons.LOCK_OUTLINED

        self.icon_repeat_one = ft.icons.REPEAT_ONE

        self.icon_settings = ft.icons.SETTINGS

        self.icon_tg = ft.IconButton(icon=ft.icons.TELEGRAM,
                                     icon_color=ft.colors.WHITE)

        self.icon_yt = ft.IconButton(icon=ft.icons.ONDEMAND_VIDEO,
                                     icon_color=ft.colors.WHITE)

        self.icon_github = ft.Container(
            content=ft.Image(src='github_logo.png', width=23, height=23), margin=9)

        self.icon_email = ft.Container(
            content=ft.Image(src='email_logo.png', width=23, height=23), margin=9)

        self.icon_linkedin = ft.Container(
            content=ft.Image(src='linkedin_logo.png', width=23, height=23), margin=9)

        self.icon_inst = ft.Container(
            content=ft.Image(src='inst_logo.png', width=23, height=23), margin=9)
