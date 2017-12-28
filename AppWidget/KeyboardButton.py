#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.button import Button

class KeyboardButton(Button):
    def highlight(self):
        self.background_color = [1, 0, 0, 1]