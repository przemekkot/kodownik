import unittest
# CodesList
# if_is
from kivy.uix.gridlayout import GridLayout

from kodownik.components.Product import EmptyProduct, Product


class ProductTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_product(self):
        product = EmptyProduct()

        self.assertEqual(product.name, "Brak produktu")
        self.assertEqual(product.code, "")
        self.assertEqual(product.quantity_type, "szt")

    def test_product_from_list(self):
        product = Product([
            "Ryba",
            "szt",
            "123"
        ])

        self.assertEqual(product.name, "Ryba")
        self.assertEqual(product.code, "123")
        self.assertEqual(product.quantity_type, "szt")

    def test_product_from_args(self):
        product = Product(
            name="Ryba",
            quantity_type="szt",
            code="123"
        )

        self.assertEqual(product.name, "Ryba")
        self.assertEqual(product.code, "123")
        self.assertEqual(product.quantity_type, "szt")


if __name__ == '__main__':
    unittest.main()
