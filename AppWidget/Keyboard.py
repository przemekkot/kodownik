#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.gridlayout import GridLayout

from AppWidget.KeyboardButton import KeyboardButton


class Keyboard(GridLayout):
    numbers = ["7","8","9","4","5","6","1","2","3", "0", "00"]
    keyboard_buttons = {}

    def __init__(self, **kwargs):
        super(Keyboard, self).__init__(**kwargs)
        self.keyboard = GridLayout(rows=4, cols=3)
        self.keyboard.spacing = [5, 5]
        for number in self.numbers:
            self.keyboard_buttons[number] = KeyboardButton(text=number)
            self.keyboard.add_widget(self.keyboard_buttons[number])
        self.add_widget(self.keyboard)

    def reset_buttons(self):
        for key, button in self.keyboard_buttons.items():
            button.reset_background()

    def show_code(self, code_string):
        self.reset_buttons()
        for number in code_string:
            self.keyboard_buttons[number].highlight()