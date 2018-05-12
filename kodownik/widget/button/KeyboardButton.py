#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kodownik.widget.button.HighlightButton import HighlightButton


class KeyboardButton(HighlightButton):
    size_hint = (1, .8)
    def __init__(self, **kwargs):
        super(KeyboardButton, self).__init__(**kwargs)
        self.font_size = 30
        self.bold = True