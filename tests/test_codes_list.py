import unittest
# CodesList
# if_is
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kodownik.components.Code import Code
from kodownik.components.Product import Product
from kodownik.widget.CodesList import CodesList
from kodownik.widget.screen.ResultScreen import NUMBER_OF_TEST_CODES


class CodesListTestCase(unittest.TestCase):
    def setUp(self):
        self.codes_list = CodesList(count=NUMBER_OF_TEST_CODES)
        self.results = [self.make_result(i) for i in range(NUMBER_OF_TEST_CODES)]


    def make_result(self, number):
        """

        :param number:
        :type number: int
        :return: tuple
        """
        passed = True
        picked_code = Code(Product(
            code=str(number),
            name="Prod " + str(number),
            quantity_type="kg"))

        if number % 2 == 1:
            number = 100 - number
            passed = False

        entered_code = Code(Product(
            code=str(number),
            name="Prod " + str(number),
            quantity_type="kg"))

        return (
            picked_code,
            entered_code,
            passed
        )

    def tearDown(self):
        pass

    def test_if_is(self):
        self.assertTrue(self.codes_list)
        self.assertIsInstance(self.codes_list, GridLayout)

    def test_has_list_display(self):
        self.assertIsInstance(self.codes_list.label_list, list)

    def test_show_results(self):
        self.codes_list.show_results(self.results)

        self.assertIsInstance(self.codes_list.label_list[0], GridLayout)
        self.assertIsInstance(self.codes_list.label_list[0].name, Label)
        self.assertIsInstance(self.codes_list.label_list[0].proper_code, Label)
        self.assertIsInstance(self.codes_list.label_list[0].entered_code, Label)

        self.assertEqual(len(self.codes_list.label_list), 20)

        self.assertEqual(self.codes_list.label_list[0].passed, True)
        self.assertEqual(self.codes_list.label_list[1].passed, False)

        self.assertEqual(self.codes_list.label_list[0].proper_code.text, "0")
        self.assertEqual(self.codes_list.label_list[0].entered_code.text, "0")

        self.assertEqual(self.codes_list.label_list[1].proper_code.text, "1")
        self.assertEqual(self.codes_list.label_list[1].entered_code.text, "99")

if __name__ == '__main__':
    unittest.main()
