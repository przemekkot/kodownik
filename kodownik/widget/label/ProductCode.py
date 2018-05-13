#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.label import Label
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.utils import get_color_from_hex

GREY_COLOR = "#969696"
GREEN_COLOR = "#42ba3e"
RED_COLOR = "#f02e23"


class ProductCode(Label):
    code = None
    bold = True
    font_size = 84
    size_hint = (.3, .3)

    def __init__(self, **kwargs):
        super(ProductCode, self).__init__(**kwargs)
        self.text = ""

    def show_code(self, event, code):
        self.code = code
        self.clear_text()
        self.reset_background()
        self.setNumber(code.code)

    def setNumber(self, number):
        self.text = str(number)

    def clear_text(self):
        self.text = ""

    def make_background(self, color):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=get_color_from_hex(color))
            Rectangle(pos=self.pos, size=self.size)

    def on_size(self, *args):
        self.reset_background()

    def reset_background(self):
        self.make_background(GREY_COLOR)

    def is_right(self):
        self.make_background(GREEN_COLOR)

    def is_wrong(self):
        self.make_background(RED_COLOR)