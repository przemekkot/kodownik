#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kodownik.components.Code import Code


class TestWorkflow:
    def __init__(self, cm, product_name, product_code, screen_keyboard, submit_buttons):
        """  This is a class that will be responsible for test workflow.
            Order of functions is top-bottom, that's alse the order of the workflow.

        :param cm:
        :type cm: CodeManager

        :param product_name:
        :type product_name: ProductName

        :param product_code:
        :type product_code: ProductCode

        :param screen_keyboard:
        :type screen_keyboard: ScreenKeyboard

        :param submit_buttons:
        :type submit_buttons: SubmitButtons
        """


        self.cm = cm
        self.product_name = product_name
        self.product_code = product_code
        self.screen_keyboard = screen_keyboard
        self.submit_buttons = submit_buttons

    def pick_a_product(self):
        self.picked_code = self.cm.pick_product()
        self.show_product()

    def show_product(self):
        self.entered_code = Code()
        self.product_code.handle_product_change(None, self.entered_code)
        self.product_name.handle_product_change(self.picked_code)
        self.submit_buttons.handle_product_change(self.picked_code)
        self.screen_keyboard.handle_product_change(self.picked_code)

    def handle_user_enter_number(self, event, button_text):
        if self.screen_keyboard.button_to_be_pressed(button_text):
            self.entered_code.add_number(button_text)

            if self.entered_code == self.picked_code:
                self.submit_buttons.highlight_submit_button()
            else:
                self.show_next_number()
        else:
            self.show_product()

    def show_next_number(self):
        self.product_code.handle_product_change(None, self.entered_code)
        self.screen_keyboard.highlight_next_button()

    def handle_user_submit_code(self, event, button_pressed):
        if self.picked_code.proper_submit(button_pressed):
            self.pick_a_product()
        else:
            self.show_product()

