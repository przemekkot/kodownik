#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.gridlayout import GridLayout

from AppWidget.KodWindow import KodWindow
from AppWidget.MainMenu import MainMenu

class KodownikWindow(GridLayout):
    kod_window = KodWindow(cols=1, rows=5)
    menu_window = MainMenu(cols=1, rows=3)

    def __init__(self, **kwargs):
        super(KodownikWindow, self).__init__(**kwargs)
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