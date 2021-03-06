#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock

from kodownik.components.Code import Code
from kodownik.components.CodeManager import CodeManager
from kodownik.components.LearningWorkflow import LearningWorkflow
from kodownik.components.Product import Product
from kodownik.widget.ScreenKeyboard import ScreenKeyboard
from kodownik.widget.button.SubmitButtons import SubmitButtons
from kodownik.widget.label.ProductCode import ProductCode
from kodownik.widget.label.ProductName import ProductName


class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.test_product = Product(
            code="1",
            name="Test Product",
            quantity_type="szt"
        )
        self.test_product2 = Product(
            code="123",
            name="Test Product",
            quantity_type="szt"
        )
        self.test_product3 = Product(
            code="3",
            name="Test Product",
            quantity_type="szt"
        )
        self.test_code = Code(self.test_product)
        self.test_code2 = Code(self.test_product2)
        self.test_code3 = Code(self.test_product3)

        self.cm = CodeManager()
        self.cm.pick_product = Mock(return_value=self.test_code)

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
        self.learn.pick_a_product(None)

        picked_code = self.learn.picked_code
        entered_code = self.learn.entered_code

        self.assertEqual(entered_code.code, "")
        self.assertEqual(entered_code.name, "Brak produktu")

        self.assertEqual(picked_code.code, self.test_code.code)
        self.assertEqual(picked_code.name, self.test_code.name)


    def test_show_product(self):
        self.learn.pick_a_product(None)
        entered_code = self.learn.entered_code

        self.assertEqual(entered_code.code, "")
        self.assertEqual(entered_code.name, "Brak produktu")

        self.assertEqual(self.product_name.text, self.test_code.name)
        self.assertEqual(self.product_code.text, "")

        self.assertEqual(self.screen_keyboard.highlighted_button().text, self.test_code.code)

    def test_handle_user_enter_number(self):
        self.learn.pick_a_product(None)
        self.learn.handle_user_enter_number(None, "1")
        self.assertEqual(self.product_code.text, "1")
        self.assertEqual(self.submit_buttons.highlighted_button().value, self.test_product.quantity_type)

        self.learn.pick_a_product(None)
        self.learn.handle_user_enter_number(None, "0")
        self.assertEqual(self.product_code.text, "")
        self.assertEqual(self.submit_buttons.highlighted_button(), None)
        self.assertEqual(self.screen_keyboard.highlighted_button().text, "1")



    def test_show_next_number(self):
        self.learn.pick_a_product(None)
        self.learn.show_product(event=None, code=self.test_code2)
        self.learn.handle_user_enter_number(None, "1")

        self.assertEqual(self.product_code.text, "1")
        self.assertNotEqual(self.screen_keyboard.highlighted_button(), None)
        self.assertEqual(self.screen_keyboard.highlighted_button().text, "2")
        self.assertEqual(self.submit_buttons.highlighted_button(), None)

    def test_handle_user_submit_code(self):
        self.learn.pick_a_product(None)
        self.learn.show_product(event=None, code=self.test_code3)
        self.learn.handle_user_enter_number(None, "3")

        self.assertEqual(self.product_code.text, "3")
        self.assertEqual(self.submit_buttons.highlighted_button().value, self.test_product.quantity_type)

        self.learn.handle_user_submit_code(None, "szt")
        self.assertEqual(self.product_code.text, "")
        self.assertEqual(self.submit_buttons.highlighted_button(), None)
        self.assertEqual(self.screen_keyboard.highlighted_button().text, "1")

        self.learn.pick_a_product(None)
        self.learn.show_product(event=None, code=self.test_code3)
        self.learn.handle_user_enter_number(None, "3")

        self.assertEqual(self.product_code.text, "3")
        self.assertEqual(self.submit_buttons.highlighted_button().value, self.test_product.quantity_type)

        self.learn.handle_user_submit_code(None, "kg")
        self.assertEqual(self.product_code.text, "")
        self.assertEqual(self.submit_buttons.highlighted_button(), None)
        self.assertEqual(self.screen_keyboard.highlighted_button().text, "3")

if __name__ == '__main__':
    unittest.main()