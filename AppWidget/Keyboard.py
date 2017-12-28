#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from AppLibraries.CodePresenter import CodePresenter
from AppWidget.KeyboardButton import KeyboardButton


class Keyboard(GridLayout):
    numbers = ["7","8","9","4","5","6","1","2","3", "0", "00"]
    keyboard_buttons = {}
    code_presenter = CodePresenter()

    def __init__(self, **kwargs):
        self.code_label = kwargs['code_label']
        del kwargs['code_label']

        super(Keyboard, self).__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.keyboard = GridLayout(rows=4, cols=3)
        self.keyboard.spacing = [5, 5]

        for number in self.numbers:
            button = KeyboardButton(text=number)
            button.bind(on_press=self.show_next_button)
            self.keyboard.add_widget(button)
            self.keyboard_buttons[number] = button
        self.add_widget(self.keyboard)

    def reset_buttons(self):
        for key, button in self.keyboard_buttons.items():
            button.reset_background()

    def show_code(self, code_string):
        self.reset_buttons()
        self.code_label.clear_text()
        self.code_presenter = CodePresenter(code_string)
        self.highlight_next_button()


    def highlight_next_button(self,):
        number = self.code_presenter.next_sign()
        self.keyboard_buttons[number].highlight()

    def show_next_button(self, button):
        button.show_green()
        self.code_label.text = self.code_label.text + button.text
        try:
            self.highlight_next_button()
        except IndexError:
            pass

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        number = int(keycode[1][-1])
        if 10 > number >= 0 :
            print(number)
            self.keyboard_buttons[str(number)].dispatch("on_press")