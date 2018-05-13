#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from kodownik.components.Code import Code
from kodownik.components.WorkflowEventDispatcher import event_dispatcher
from kodownik.widget.button.KeyboardButton import KeyboardButton


class ScreenKeyboard(GridLayout):
    size_hint = (.5, .8)
    numbers = ["7","8","9","4","5","6","1","2","3", "0", "00"]
    keyboard_buttons = {}
    code = None

    def __init__(self, **kwargs):
        # code_dispatcher.bind(on_product_change=self.handle_product_change)
        super(ScreenKeyboard, self).__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.keyboard = GridLayout(rows=4, cols=3)
        self.keyboard.spacing = [5, 5]

        for number in self.numbers:
            button = KeyboardButton(text=number)
            # dispatch number on button press
            button.bind(on_press=self.send_user_number)
            self.keyboard.add_widget(button)
            self.keyboard_buttons[number] = button
        self.add_widget(self.keyboard)

    def reset_buttons(self):
        for key, button in self.keyboard_buttons.items():
            button.reset_background()

    def send_user_number(self, button):
        event_dispatcher.do_handle_user_enter_number(button.text)

    def show_new_code(self, code):
        self.reset_buttons()
        self.code = code
        self.highlight_next_button(self.code.highlight_number)

    def highlight_next_button(self, number = None):
        self.reset_buttons()
        if not number:
            self.code.get_next_number()
            number = self.code.highlight_number

        if number != None:
            try:
                self.keyboard_buttons[str(number)].highlight()
            except Exception as e:
                pass

    def highlighted_button(self):
        number = self.code.highlight_number
        return self.keyboard_buttons[str(number)]

    def show_next_button(self, button):
        pass
        # if not button.to_be_pressed:
        #     self.show_code(self.code_manager.code)
        #     return
        #
        # button.show_green(self.code_manager.code.sign_shown)
        # self.code_label.text = self.code_label.text + button.text
        # try:
        #     self.highlight_next_button()
        # except IndexError:
        #     if self.code_manager.code.is_code_right(self.code_label.text):
        #         self.code_label.is_right()
        #     else:
        #         self.code_label.is_wrong()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        try:
            number = int(keycode[1][-1])
            if 10 > number >= 0 :
                self.keyboard_buttons[str(number)].dispatch("on_press")
        except ValueError:
            pass