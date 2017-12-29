#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.label import Label
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

class CodeNameLabel(Label):
    font_size = 40
    size_hint = (.3, .3)

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(59/255,	118/255,	191/255, 1)
            Rectangle(pos=self.pos, size=self.size)