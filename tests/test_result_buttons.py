import unittest
# ResultButtonsTestCase
# my_function
from kodownik.widget.button.ResultButtons import ResultButtons


class ResultButtonsTestCase(unittest.TestCase):
    def setUp(self):
        self.result_buttons = ResultButtons()

    def tearDown(self):
        pass

    def test_if_is(self):
        self.assertTrue(self.result_buttons)

    def test_has_back_button(self):
        self.assertTrue(self.result_buttons.back_button)

    def test_has_repeat_button(self):
        self.assertTrue(self.result_buttons.repeat_button)

    def test_go_back(self):
        self.assertTrue(self.result_buttons.go_back())

    def test_repeat(self):
        self.assertTrue(self.result_buttons.repeat_test())

if __name__ == '__main__':
    unittest.main()
