#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from AppLibraries.Codes import Codes


class KodWindow(GridLayout):
    padding = VariableListProperty(100)
    spacing = VariableListProperty(50, length=2)

    name_label = Label(text="Nazwa kodu")
    code_label = Label(text="123")
    next_code_button = Button(text="Następny kod")

    def __init__(self, **kwargs):
        super(KodWindow, self).__init__(**kwargs)
        self.add_widget(self.name_label)
        self.add_widget(self.code_label)
        self.add_widget(self.next_code_button)

        self.next_code_button.bind(on_press=self.choose_next_code)

    def choose_next_code(self, button_instance):
            codes_for_fruits = Codes("Data/kody_produktow_owoce.csv")
            code = codes_for_fruits.pick_one()
            self.name_label.text = code[0]
            self.code_label.text = code[2]