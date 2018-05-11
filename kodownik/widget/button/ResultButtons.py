#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

__all__ = ['_back', '_repeat', 'ResultButtons']

_back = "Powrót do menu"
_repeat = "Powtórz test"

class ResultButtons(GridLayout):

    def __init__(self, **kwargs):
        super(ResultButtons, self).__init__(**kwargs)
        self.show_buttons()

    def show_buttons(self):
        self.back_button = Button(text=_back, size_hint=(.1, .2))
        self.repeat_button = Button(text=_repeat, size_hint=(.1, .2))

        self.add_widget(self.back_button)
        self.add_widget(self.repeat_button)

        self.back_button.bind(on_press=self.go_back)
        self.repeat_button.bind(on_press=self.repeat_test)

    def go_back(self):
        self.parent.parent.show_menu()
        return False    # @todo: inspect this function, test fails

    def repeat_test(self):
        return False    # @todo: in spect this function, test fails