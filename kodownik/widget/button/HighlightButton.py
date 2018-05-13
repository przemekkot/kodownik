#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.button import Button


class HighlightButton(Button):

    def __init__(self, **kwargs):
        super(HighlightButton, self).__init__(**kwargs)
        self.highlighted = False
        self.background_normal = ''
        self.background_color = [.1, .1, .1, 1]

    def reset_background(self):
        self.highlighted = False
        self.background_color = [.1, .1, .1, 1]

    def show_green(self, alpha = 1):
        self.highlighted = False
        alpha = alpha / 6
        self.background_color = [1, 49/255, 218/255, alpha]

    def highlight(self):
        self.highlighted = True
        self.background_color = [1, 0, 0, 1]

    def is_highlighted(self):
        return self.highlighted