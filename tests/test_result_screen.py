import unittest
# ResultScreenTestCase
# test_if_is
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kodownik.widget.screen.ResultScreen import ResultScreen


class ResultScreenTestCase(unittest.TestCase):
    def setUp(self):
        self.result_screen = ResultScreen()
        pass

    def tearDown(self):
        pass

    def test_if_is(self):
        self.assertTrue(self.result_screen)

    def test_if_has_test_results(self):
        self.assertTrue(self.result_screen.test_result)
        self.assertIsInstance(
            self.result_screen.test_result,
            GridLayout
        )

    def test_if_has_test_codes_list(self):
        self.assertTrue(self.result_screen.codes_list)
        self.assertIsInstance(
            self.result_screen.codes_list,
            GridLayout
        )

    def test_if_has_results_buttons(self):
        self.assertTrue(self.result_screen.result_buttons)
        self.assertIsInstance(
            self.result_screen.test_codes,
            GridLayout
        )

        self.assertIsInstance(
            self.result_screen.test_codes.repeat,
            Button
        )

        self.assertIsInstance(
            self.result_screen.test_codes.back,
            Button
        )



if __name__ == '__main__':
    unittest.main()
