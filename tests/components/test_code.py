import unittest
# CodesList
# if_is
from kivy.uix.gridlayout import GridLayout

from kodownik.components.Code import Code
from kodownik.components.Product import EmptyProduct, Product


class CodeTestCase(unittest.TestCase):
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

    def test_code(self):
        for product in [self.test_product_1, self.test_product_2]:
            code = Code(product)

            self.assertEqual(product.code, code.code)
            self.assertEqual(product.name, code.name)
            self.assertEqual(product.quantity_type, code.quantity)

    def test_get_first_number(self):
        code = Code(self.test_product_2)
        self.assertEqual(code.highlight_number, "2")

        number = code.get_first_number()
        self.assertEqual(number, "3")

        number = code.get_first_number()
        self.assertEqual(number, "4")

        number = code.get_first_number()
        self.assertEqual(number, None)

    def test_get_next_number(self):
        code = Code(self.test_product_2)
        self.assertEqual(code.highlight_number, "2")

        code.get_next_number()
        self.assertEqual(code.highlight_number, "3")

        code.get_next_number()
        self.assertEqual(code.highlight_number, "4")

        code.get_next_number()
        self.assertEqual(code.highlight_number, None)

    def test_equals(self):
        code1 = Code(self.test_product_1)
        code2 = Code(self.test_product_2)

        self.assertFalse(code1 == code2)

        code1.code = "123"
        code2.code = "123"

        self.assertTrue(code1 == code2)

if __name__ == '__main__':
    unittest.main()
