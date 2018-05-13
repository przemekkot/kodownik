import unittest
# CodesList
# if_is
from kivy.uix.gridlayout import GridLayout

from kodownik.components.Code import Code
from kodownik.components.Product import EmptyProduct, Product
from kodownik.widget.ScreenKeyboard import ScreenKeyboard


class ScreenKeyboardTestCase(unittest.TestCase):
    def setUp(self):
        self.test_product_1 = Product(
            code="123456",
            name="Product 1",
            quantity_type="szt"
        )
        self.test_product_2 = Product(
            code="234",
            name="Product 2",
            quantity_type="kg"
        )
        pass

    def tearDown(self):
        pass

    def test_screen_keyboard(self):
        screen_keyboard = ScreenKeyboard()
        self.assertTrue(screen_keyboard)

    def test_show_new_code(self):
        screen_keyboard = ScreenKeyboard()
        screen_keyboard.show_new_code(Code(self.test_product_1))

        button = screen_keyboard.highlighted_button()
        self.assertEqual(button.text, "1")

        screen_keyboard.highlight_next_button()
        button = screen_keyboard.highlighted_button()
        self.assertEqual(button.text, "2")

    def test_reset_buttons(self):
        screen_keyboard = ScreenKeyboard()
        screen_keyboard.show_new_code(Code(self.test_product_1))

        button = screen_keyboard.highlighted_button()
        self.assertEqual(button.text, "1")

        screen_keyboard.reset_buttons()
        self.assertFalse(button.is_highlighted())


if __name__ == '__main__':
    unittest.main()
