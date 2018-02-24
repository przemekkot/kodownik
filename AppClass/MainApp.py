#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App

from AppWidget.KodownikWindow import KodownikWindow

class MainApp(App):
    def build(self):
        self.title = 'MainApp'
        return KodownikWindow(cols=1, rows=1)