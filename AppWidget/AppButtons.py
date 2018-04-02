#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


_back = "Powrót"
_next_code = "Następny kod"
_no_code_name = "Brak kodu"
_empty_string = ""
_no_code = ""

EMPTY_CODE = [_no_code_name, _empty_string, _no_code]

class AppButtons(GridLayout):

    next_code_button = Button(text=_next_code, size_hint=(.3, .3))
    back_button = Button(text=_back, size_hint=(.3, .3))


    def __init__(self, code_manager=None, **kwargs):
        super(AppButtons, self).__init__(**kwargs)
        self.show_buttons()
        self.code_manager = code_manager

    def show_buttons(self):
        self.add_widget(self.back_button)
        self.add_widget(self.next_code_button)
        self.next_code_button.bind(on_press=self.choose_next_code)
        self.back_button.bind(on_press=self.go_back_to_main_menu)

    def go_back_to_main_menu(self, back_button):
        self.parent.parent.show_menu()

    def choose_next_code(self, button_instance):
        self.code_manager.pick_product()