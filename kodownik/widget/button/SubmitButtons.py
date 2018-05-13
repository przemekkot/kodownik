#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.properties import VariableListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kodownik.components.WorkflowEventDispatcher import event_dispatcher
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

        self.plu_button.bind("on_press", self.submit_code)
        self.waga_button.bind("on_press", self.submit_code)

        self.add_widget(self.plu_button)
        self.add_widget(self.waga_button)

    def submit_code(self, button):
        event_dispatcher.do_handle_user_submit_code(None, button.value)

    def reset_buttons(self):
        self.plu_button.reset_background()
        self.waga_button.reset_background()

    def highlight_submit_button(self, code):
        self.reset_buttons()
        if code.quantity == self.plu_button.value:
            self.plu_button.highlight()

        if code.quantity == self.waga_button.value:
            self.waga_button.highlight()

    def highlighted_button(self):
        if self.plu_button.highlighted:
            return self.plu_button

        if self.waga_button.highlighted:
            return self.waga_button

        return None