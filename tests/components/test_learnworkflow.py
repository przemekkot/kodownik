#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from kodownik.components.CodeManager import CodeManager
from kodownik.components.LearningWorkflow import LearningWorkflow
from kodownik.widget.ScreenKeyboard import ScreenKeyboard
from kodownik.widget.button.SubmitButtons import SubmitButtons
from kodownik.widget.label.ProductCode import ProductCode
from kodownik.widget.label.ProductName import ProductName


class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.cm = CodeManager()
        self.product_name = ProductName()
        self.product_code = ProductCode()
        self.screen_keyboard = ScreenKeyboard()
        self.submit_buttons = SubmitButtons()

        self.learn = LearningWorkflow(
            cm = self.cm,
            product_code=self.product_code,
            product_name=self.product_name,
            screen_keyboard=self.screen_keyboard,
            submit_buttons=self.submit_buttons
        )

        pass

    def tearDown(self):
        pass

    def test_pick_a_product(self):
        self.assertTrue(False)

    def test_show_product(self):
        self.assertTrue(False)

    def handle_user_enter_number(self):
        self.assertTrue(False)

    def show_next_number(self):
        self.assertTrue(False)

    def handle_user_submit_code(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()