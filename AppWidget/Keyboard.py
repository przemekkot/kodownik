#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Keyboard(GridLayout):
    numbers = ["7","8","9","4","5","6","1","2","3", "0", "00"]
    keys = {}

    def __init__(self, **kwargs):
        super(Keyboard, self).__init__(**kwargs)
        self.keyboard = GridLayout(rows=4, cols=3)
        self.keyboard.spacing = [5, 5]
        for number in self.numbers:
            self.keys[number] = Button(text=number, background_color=[1, 0, 0, 1])
            self.keyboard.add_widget(self.keys[number])
        self.add_widget(self.keyboard)