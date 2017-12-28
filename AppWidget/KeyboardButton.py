#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.button import Button

class KeyboardButton(Button):
    def __init__(self, **kwargs):
        super(KeyboardButton, self).__init__(**kwargs)
        self.register_event_type("on_next_code")
        self.background_color = [0, 0, 0, 1]

    def on_next_code(self):
        self.reset_background()

    def reset_background(self):
        self.background_color = [0, 0, 0, 1]

    def highlight(self):
        self.background_color = [1, 0, 0, 1]