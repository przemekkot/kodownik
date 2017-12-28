#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App

from AppWidget.Container import Container

class MainApp(App):
    def build(self):
        self.title = 'MainApp'
        return Container(cols=1, rows=1)