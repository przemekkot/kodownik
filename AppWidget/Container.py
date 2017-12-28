#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.gridlayout import GridLayout

from AppWidget.KodWindow import KodWindow

class Container(GridLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.add_widget(KodWindow(cols=1, rows=4))