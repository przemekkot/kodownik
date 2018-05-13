import unittest
# ResultButtonsTestCase
# my_function
from kodownik.components.Code import Code
from kodownik.components.Product import Product
from kodownik.widget.button.ResultButtons import ResultButtons
from kodownik.widget.button.SubmitButtons import SubmitButtons


class SubmitButtonsTestCase(unittest.TestCase):
    def setUp(self):
        self.submit_buttons = SubmitButtons()
        self.test_code_plu = Code(Product(
            code="123",
            name="None",
            quantity_type="szt"
        ))

        self.test_code_waga = Code(Product(
            code="123",
            name="None",
            quantity_type="kg"
        ))

    def tearDown(self):
        pass

    def test_if_is(self):
        self.assertTrue(self.submit_buttons)

    def test_has_plu_button(self):
        self.assertTrue(self.submit_buttons.plu_button)

    def test_has_waga_button(self):
        self.assertTrue(self.submit_buttons.waga_button)

    def test_highlights_and_reset(self):
        plu_button = self.submit_buttons.plu_button
        waga_button = self.submit_buttons.waga_button

        self.submit_buttons.reset_buttons()

        self.assertFalse(plu_button.highlighted)
        self.assertFalse(waga_button.highlighted)

        self.submit_buttons.highlight_submit_button(self.test_code_plu)

        self.assertTrue(plu_button.highlighted)
        self.assertFalse(waga_button.highlighted)

        self.submit_buttons.highlight_submit_button(self.test_code_waga)

        self.assertFalse(plu_button.highlighted)
        self.assertTrue(waga_button.highlighted)

    def test_highlighted_button(self):
        plu_button = self.submit_buttons.plu_button
        waga_button = self.submit_buttons.waga_button

        self.submit_buttons.highlight_submit_button(self.test_code_plu)
        self.assertEqual(plu_button, self.submit_buttons.highlighted_button())

        self.submit_buttons.highlight_submit_button(self.test_code_waga)
        self.assertEqual(waga_button, self.submit_buttons.highlighted_button())

        self.submit_buttons.reset_buttons()
        self.assertEqual(None, self.submit_buttons.highlighted_button())


if __name__ == '__main__':
    unittest.main()
