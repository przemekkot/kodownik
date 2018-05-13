#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kodownik.components.Code import Code
from kodownik.components.WorkflowEventDispatcher import event_dispatcher
from kodownik.components.Workflow import Workflow


class  LearningWorkflow(Workflow):
    picked_code=None
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

        event_dispatcher.bind(on_pick_a_product=self.pick_a_product)
        event_dispatcher.bind(on_show_product=self.show_product)
        event_dispatcher.bind(on_handle_user_enter_number=self.handle_user_enter_number)
        event_dispatcher.bind(on_show_next_number=self.show_next_number)
        event_dispatcher.bind(on_handle_user_submit_code=self.handle_user_submit_code)


    def pick_a_product(self, event=None):
        self.picked_code = self.cm.pick_product()
        event_dispatcher.do_show_product(self.picked_code)

    def show_product(self, event=None, code=None):
        self.picked_code = code
        self.entered_code = Code()
        self.product_code.handle_product_change(None, self.entered_code)
        self.product_name.handle_product_change(None, self.picked_code)
        self.submit_buttons.handle_product_change(self.picked_code)
        self.screen_keyboard.show_new_code(self.picked_code)

    def handle_user_enter_number(self, number, event=None):
        self.picked_code = self.screen_keyboard.code
        if self.screen_keyboard.highlighted_button().text == number:
            self.entered_code.add_number(number)

            if self.entered_code == self.picked_code:
                self.submit_buttons.highlight_submit_button()
            else:
                event_dispatcher.do_show_next_number()
        else:
            event_dispatcher.do_show_product(self.screen_keyboard.code)

    def show_next_number(self, event=None):
        self.product_code.handle_product_change(None, self.entered_code)
        self.screen_keyboard.highlight_next_button()

    def handle_user_submit_code(self, quantity, event=None):
        if self.picked_code.has_quantity(quantity):
            event_dispatcher.do_pick_a_product()
        else:
            event_dispatcher.do_show_product()

