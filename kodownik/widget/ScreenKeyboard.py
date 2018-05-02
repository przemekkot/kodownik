#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from kodownik.components.Code import Code
from kodownik.components.CodeEventDispatcher import code_dispatcher
from kodownik.widget.button.KeyboardButton import KeyboardButton


class ScreenKeyboard(GridLayout):
    size_hint = (.5, .8)
    numbers = ["7","8","9","4","5","6","1","2","3", "0", "00"]
    keyboard_buttons = {}
    code_presenter = Code()

    def __init__(self, code_label=None, code_manager=None, **kwargs):
        code_dispatcher.bind(on_product_change=self.handle_product_change)
        self.code_label = code_label
        self.code_manager = code_manager
        super(ScreenKeyboard, self).__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.keyboard = GridLayout(rows=4, cols=3)
        self.keyboard.spacing = [5, 5]

        for number in self.numbers:
            button = KeyboardButton(text=number)
            button.bind(on_press=self.dispatch_number_entered)
            self.keyboard.add_widget(button)
            self.keyboard_buttons[number] = button
        self.add_widget(self.keyboard)

    def reset_buttons(self):
        for key, button in self.keyboard_buttons.items():
            button.reset_background()

    def handle_product_change(self, event, code):
        self.show_code(code)

    def dispatch_number_entered(self, button):
        code_dispatcher.dispatch_number_event(button.text)

    def show_code(self, code):
        self.reset_buttons()
        self.code_presenter = code
        self.highlight_next_button()

    def highlight_next_button(self):
        self.keyboard_buttons[self.code_presenter.highlight_numbers[-1]].highlight()

    def show_next_button(self, button):
        if not button.to_be_pressed:
            self.show_code(self.code_manager.code)
            return

        button.show_green(self.code_manager.code.sign_shown)
        self.code_label.text = self.code_label.text + button.text
        try:
            self.highlight_next_button()
        except IndexError:
            if self.code_manager.code.is_code_right(self.code_label.text):
                self.code_label.is_right()
            else:
                self.code_label.is_wrong()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "enter":
            self.code_manager.pick_product()
        try:
            number = int(keycode[1][-1])
            if 10 > number >= 0 :
                self.keyboard_buttons[str(number)].dispatch("on_press")
        except ValueError:
            pass