#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.label import Label
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle


class CodeLabel(Label):
    def clear_text(self):
        self.text = ""

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 1, 0, 0.25)
            Rectangle(pos=self.pos, size=self.size)