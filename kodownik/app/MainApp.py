#!/usr/bin/env python
# -*- coding: utf-8 -*-


from kivy.app import App
from kodownik.widget.screen.MenuScreen import MenuScreen


class MainApp(App):
    def build(self):
        self.title = 'MainApp'
        return MenuScreen(cols=1, rows=1)