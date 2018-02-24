#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

_learn = "Nauka"
_test  = "Test"
_exit = "Wyjście"

class MainMenu(GridLayout):
    padding = VariableListProperty(100)
    spacing = VariableListProperty(10, length=2)

    learn_button = Button(text=_learn, size_hint=(.3, .3))
    test_button = Button(text=_test, size_hint=(.3, .3))
    exit_button = Button(text=_exit, size_hint=(.3, .3))

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.show_menu()

    def show_menu(self):
        self.add_widget(self.learn_button)
        self.add_widget(self.test_button)
        self.add_widget(self.exit_button)

        self.learn_button.bind(on_press=self.begin_learning)
        self.test_button.bind(on_press=self.begin_test)
        self.exit_button.bind(on_press=self.exit_app)

    def begin_learning(self, learn_button):
        kodownik_window = self.parent
        kodownik_window.show_learning_screen()
        pass

    def begin_test(self, test_button):
        kodownik_window = self.parent
        kodownik_window.show_testing_screen()

    def exit_app(self, exit_button):
        App.get_running_app().stop()