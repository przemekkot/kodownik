#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

_plu = "PLU"
_waga  = "Waga"

class SubmitButtons(GridLayout):

    plu_button = Button(text=_plu, size_hint=(.1, .2))
    waga_button = Button(text=_waga, size_hint=(.1, .2))

    def __init__(self, **kwargs):
        super(SubmitButtons, self).__init__(**kwargs)
        self.show_buttons()

    def show_buttons(self):
        self.add_widget(self.plu_button)
        self.add_widget(self.waga_button)