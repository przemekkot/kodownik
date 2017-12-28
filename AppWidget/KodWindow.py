#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from AppLibraries.Codes import Codes
from AppWidget.CodeLabel import CodeLabel
from AppWidget.CodeNameLabel import CodeNameLabel
from AppWidget.Keyboard import Keyboard

_no_code_name = "Brak kodu"
_choose_code = "Wybierz kod"
_next_code = "Następny kod"
_empty_string = ""
_no_code = ""

EMPTY_CODE = [_no_code_name, _empty_string, _no_code]

class KodWindow(GridLayout):
    padding = VariableListProperty(100)
    spacing = VariableListProperty(10, length=2)

    name_label = CodeNameLabel(text=_choose_code, font_size=30, size_hint=(.5,.5))
    keyboard = Keyboard(cols=1, rows=1)
    next_code_button = Button(text=_next_code, size_hint=(.3, .3))

    codes = Codes()

    def __init__(self, **kwargs):
        super(KodWindow, self).__init__(**kwargs)

        self.add_widget(self.name_label)
        self.add_widget(self.keyboard)
        self.add_widget(self.next_code_button)

        self.next_code_button.bind(on_press=self.choose_next_code)

    def set_new_code(self, code):
        code_name = str(code[0])
        code = str(code[2])

        self.name_label.text = code_name.upper().strip()
        self.keyboard.show_code(code.strip())

    def choose_next_code(self, button_instance):
        try:
            self.set_new_code(self.codes.pick_random())
        except IndexError:
            self.set_new_code(EMPTY_CODE)