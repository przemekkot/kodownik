#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import VariableListProperty
from kivy.uix.gridlayout import GridLayout

from kodownik.components.CodeManager import CodeManager
from kodownik.widget.AppButtons import AppButtons
from kodownik.widget.ProductCode import ProductCode
from kodownik.widget.ProductName import ProductName
from kodownik.widget.ScreenKeyboard import ScreenKeyboard
from kodownik.widget.SubmitButtons import SubmitButtons


class CodeScreen(GridLayout):
    padding = VariableListProperty(100)
    spacing = VariableListProperty(10, length=2)
    code_manager = CodeManager()

    product_name = ProductName()
    product_code = ProductCode()
    screen_keyboard = ScreenKeyboard(cols=1, rows=1, code_label=product_code, code_manager=code_manager)
    submit_buttons = SubmitButtons(cols=2, rows=1, size_hint=(1, .3))
    app_buttons = AppButtons(cols=2, rows=1, size_hint=(1, .3), code_manager=code_manager)

    def __init__(self, **kwargs):
        super(CodeScreen, self).__init__(**kwargs)

        self.add_widget(self.product_code)
        self.add_widget(self.screen_keyboard)
        self.add_widget(self.submit_buttons)
        self.add_widget(self.product_name)
        self.add_widget(self.app_buttons)

