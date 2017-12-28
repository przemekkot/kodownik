#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class KodWindow(GridLayout):
    padding = VariableListProperty(100)
    spacing = VariableListProperty(50, length=2)

    name_label = Label(text="Nazwa")
    code_label = Label(text="123")
    next_code_button = Button(text="Next")

    def __init__(self, **kwargs):
        super(KodWindow, self).__init__(**kwargs)
        self.add_widget(self.name_label)
        self.add_widget(self.code_label)
        self.add_widget(self.next_code_button)