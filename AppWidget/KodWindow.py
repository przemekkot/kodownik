#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from AppLibraries.Codes import Codes
from AppWidget.CodeLabel import CodeLabel
from AppWidget.CodeNameLabel import CodeNameLabel

_no_code_name = "Brak kodu"
_choose_code = "Wybierz kod"
_next_code = "Następny kod"
_empty_string = ""
_no_code = ""

FRUIT_CODES_FILE = "Data/kody_produktow_owoce.csv"
VEGETABLES_CODES_FILE = "Data/kody_produktow_warzywa.csv"
BREAD_CODES_FILE = "Data/kody_produktow_pieczywo.csv"

EMPTY_CODE = [_no_code_name, _empty_string, _no_code]


class KodWindow(GridLayout):
    padding = VariableListProperty(100)
    spacing = VariableListProperty(10, length=2)

    name_label = CodeNameLabel(text=_choose_code, font_size=30, size_hint=(.5,.5))

    code_label = CodeLabel(text=_empty_string, bold=True, font_size=84)
    next_code_button = Button(text=_next_code, size_hint=(.3, .3))

    codes_for_fruits = Codes(FRUIT_CODES_FILE)

    def __init__(self, **kwargs):
        super(KodWindow, self).__init__(**kwargs)


        self.add_widget(self.name_label)
        self.add_widget(self.code_label)
        self.add_widget(self.next_code_button)

        self.next_code_button.bind(on_press=self.choose_next_code)

    def set_new_code(self, code):
        code_name = str(code[0])
        code = str(code[2])

        self.name_label.text = code_name.upper().strip()
        self.code_label.text = code.strip()

    def choose_next_code(self, button_instance):
        try:
            self.set_new_code(self.codes_for_fruits.pick_random())
        except IndexError:
            self.set_new_code(EMPTY_CODE)