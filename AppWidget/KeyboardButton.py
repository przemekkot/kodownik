#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.button import Button

class KeyboardButton(Button):
    size_hint = (1, .8)
    def __init__(self, **kwargs):
        super(KeyboardButton, self).__init__(**kwargs)

        self.to_be_pressed = False
        self.background_color = [.1, .1, .1, 1]
        self.font_size = 30
        self.bold = True

    def reset_background(self):
        self.to_be_pressed = False
        self.background_color = [.1, .1, .1, 1]

    def show_green(self, alpha_divider):
        self.to_be_pressed = False
        self.alpha = 1 / alpha_divider
        self.background_color = [0/255, 102/255, 34/255, self.alpha]

    def highlight(self):
        self.to_be_pressed = True
        self.background_color = [1, 0, 0, 1]