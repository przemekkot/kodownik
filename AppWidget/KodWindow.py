#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from AppLibraries.CodeManager import CodeManager
from AppLibraries.CodeLists import CodeLists
from AppWidget.AppButtons import AppButtons
from AppWidget.CodeNumber import CodeNumber
from AppWidget.CodeName import CodeName
from AppWidget.Keyboard import Keyboard
from AppWidget.SubmitButtons import SubmitButtons



class KodWindow(GridLayout):
    padding = VariableListProperty(100)
    spacing = VariableListProperty(10, length=2)
    code_manager = CodeManager()

    code_name = CodeName()
    code_number = CodeNumber()
    keyboard = Keyboard(cols=1, rows=1, code_label=code_number)
    submit_buttons = SubmitButtons(cols=2, rows=1, size_hint=(1, .3))
    app_buttons = AppButtons(cols=2, rows=1, size_hint=(1, .3))

    def __init__(self, **kwargs):
        super(KodWindow, self).__init__(**kwargs)

        self.add_widget(self.code_number)
        self.add_widget(self.keyboard)
        self.add_widget(self.submit_buttons)
        self.add_widget(self.code_name)
        self.add_widget(self.app_buttons)