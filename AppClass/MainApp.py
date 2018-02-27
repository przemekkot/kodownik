#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App

from AppWidget.MenuScreen import AppWindow

class MainApp(App):
    def build(self):
        self.title = 'MainApp'
        return AppWindow(cols=1, rows=1)