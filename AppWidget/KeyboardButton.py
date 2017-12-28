#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.button import Button

class KeyboardButton(Button):
    def __init__(self, **kwargs):
        super(KeyboardButton, self).__init__(**kwargs)
        self.background_color = [.1, .1, .1, 1]

    def reset_background(self):
        self.background_color = [.1, .1, .1, 1]

    def highlight(self):
        self.background_color = [1, 0, 0, 1]