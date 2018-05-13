#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.label import Label
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.utils import get_color_from_hex

from kodownik.components.WorkflowEventDispatcher import event_dispatcher

GREY_COLOR = "#969696"
GREEN_COLOR = "#42ba3e"
RED_COLOR = "#f02e23"


class ProductCode(Label):
    bold = True
    font_size = 84
    size_hint = (.3, .3)

    def __init__(self, **kwargs):
        event_dispatcher.bind(on_product_change=self.handle_product_change)
        event_dispatcher.bind(on_code_change=self.handle_code_change)
        super(ProductCode, self).__init__(**kwargs)
        self.text = ""

    def handle_product_change(self, event, code):
        self.clear_text()
        self.reset_background()
        self.setNumber("")

    def handle_code_change(self, event, code):
        self.clear_text()
        self.reset_background()
        self.setNumber(code.get_user_code())
        if code.is_right:
            self.is_right()
        if code.is_wrong:
            self.is_wrong()

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