#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

from kodownik.components.WorkflowEventDispatcher import event_dispatcher

_choose_code = "Wybierz kod"

class ProductName(Label):
    font_size = 40
    size_hint = (.3, .3)

    def __init__(self, **kwargs):
        event_dispatcher.bind(on_product_change=self.handle_product_change)
        super(ProductName, self).__init__(**kwargs)

    def handle_product_change(self, event, code):
        self.setName(code.name)

    def setName(self, name):
        self.text = name

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(59/255,	118/255,	191/255, 1)
            Rectangle(pos=self.pos, size=self.size)