#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

_choose_code = "Wybierz kod"

class CodeName(Label):
    font_size = 40
    size_hint = (.3, .3)

    def setName(self, name):
        self.text = name

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(59/255,	118/255,	191/255, 1)
            Rectangle(pos=self.pos, size=self.size)