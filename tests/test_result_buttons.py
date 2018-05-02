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



if __name__ == '__main__':
    unittest.main()
