#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kodownik.widget.button.HighlightButton import HighlightButton

_plu = "PLU"
_waga  = "Waga"

class SubmitButtons(GridLayout):

    def __init__(self, **kwargs):
        super(SubmitButtons, self).__init__(**kwargs)
        self.show_buttons()

    def show_buttons(self):
        self.plu_button = HighlightButton(text=_plu, size_hint=(.1, .2))
        self.waga_button = HighlightButton(text=_waga, size_hint=(.1, .2))
        self.plu_button.value = "szt"
        self.waga_button.value = "kg"


        self.add_widget(self.plu_button)
        self.add_widget(self.waga_button)

    def reset_buttons(self):
        self.plu_button.reset_background()
        self.waga_button.reset_background()

    def handle_product_change(self, code):
        self.reset_buttons()
        if code.product.quantity_type == self.plu_button.value:
            self.plu_button.highlight()

        if code.product.quantity_type == self.waga_button.value:
            self.waga_button.highlight()

    def highlighted_button(self):
        if self.plu_button.highlighted:
            return self.plu_button

        if self.waga_button.highlighted:
            return self.waga_button

        return None