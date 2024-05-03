import flet as ft

from components.button.styles import ButtonStyles
from components.icon.icon import Icons


class IconButtons:
    def __init__(self):
        self.button_icon_lock = ft.IconButton(
            icon=Icons().icon_lock,
            icon_color=ft.colors.GREY_500,
            disabled=True,
            bottom=0,
            right=0)
    
        self.button_icon_repeat_one = ft.IconButton(
            icon=Icons().icon_repeat_one,
            style=ButtonStyles().button_style_disabled,
            disabled=True,
            top=0,
            right=0,
            offset=(0.1, -0.1))
    
        self.button_icon_settings = ft.IconButton(
            icon=Icons().icon_settings,
            style=ButtonStyles().button_style_enabled,
            disabled=False,
            top=0,
            right=0,
            offset=(0.1, -0.1))
