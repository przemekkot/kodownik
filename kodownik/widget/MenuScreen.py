#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.gridlayout import GridLayout

from kodownik.widget.CodeScreen import CodeScreen
from kodownik.widget.MainMenu import MainMenu


class MenuScreen(GridLayout):
    kod_window = CodeScreen(cols=1, rows=5)
    menu_window = MainMenu(cols=1, rows=3)

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.show_menu()

    def show_menu(self):
        self.clear_widgets()
        self.add_widget(self.menu_window)

    def show_learning_screen(self):
        self.clear_widgets()
        self.add_widget(self.kod_window)

    def show_testing_screen(self):
        self.clear_widgets()
        self.add_widget(self.kod_window)