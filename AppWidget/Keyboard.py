#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Keyboard(GridLayout):
    numbers = ["9","8","7","6","5","4","3","2","1", "0", "00"]
    keys = {}

    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        self.keyboard = GridLayout(rows=4, cols=3)
        for number in self.numbers:
            self.keys[number] = Button(text=number)
            self.keyboard.add_widget(self.keys[number])

    def build(self):
        return self.keyboard