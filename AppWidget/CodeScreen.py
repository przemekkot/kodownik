#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from AppLibraries.CodeManager import CodeManager
from AppWidget.AppButtons import AppButtons
from AppWidget.ProductCode import ProductCode
from AppWidget.ProductName import ProductName
from AppWidget.ScreenKeyboard import ScreenKeyboard
from AppWidget.SubmitButtons import SubmitButtons
from AppLibraries.CodeEventDispatcher import code_dispatcher


class CodeScreen(GridLayout):
    padding = VariableListProperty(100)
    spacing = VariableListProperty(10, length=2)
    code_manager = CodeManager()

    code_name = ProductName()
    code_number = ProductCode()
    keyboard = ScreenKeyboard(cols=1, rows=1, code_label=code_number, code_manager=code_manager)
    submit_buttons = SubmitButtons(cols=2, rows=1, size_hint=(1, .3))
    app_buttons = AppButtons(cols=2, rows=1, size_hint=(1, .3), code_manager=code_manager)

    def __init__(self, **kwargs):
        super(CodeScreen, self).__init__(**kwargs)
        print("I will bind something") # @todo: move event binding to elements
        # code_dispatcher.bind(on_code_change=self.code_number.handle_code_change)
        code_dispatcher.bind(on_product_change=self.code_name.handle_product_change)
        code_dispatcher.bind(on_product_change=self.keyboard.handle_product_change)
        code_dispatcher.bind(on_product_change=self.code_number.handle_product_change)
        self.add_widget(self.code_number)
        self.add_widget(self.keyboard)
        self.add_widget(self.submit_buttons)
        self.add_widget(self.code_name)
        self.add_widget(self.app_buttons)

