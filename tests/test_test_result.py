import unittest
# TestResultTestCase
# if_is
from kivy.uix.label import Label

from kodownik.widget.TestResult import TestResult


class TestResultTestCase(unittest.TestCase):
    def setUp(self):
        self.test_result = TestResult()
        self.test_result_passed = {
            'passed' : True,
            'result' : "90%"
        }

        self.test_result_failed = {
            'passed' : False,
            'result' : "20%"
        }

    def tearDown(self):
        pass

    def test_if_is(self):
        self.assertTrue(self.test_result)

    def test_has_status_label(self):
        self.assertTrue(self.test_result.status)
        self.assertIsInstance(self.test_result.status, Label)

    def test_has_result_label(self):
        self.assertTrue(self.test_result.result)
        self.assertIsInstance(self.test_result.result, Label)

    def test_result_display(self):
        self.test_result.show_result(self.test_result_passed)
        self.assertEqual(self.test_result.status.text, "Zdałeś")
        self.assertEqual(self.test_result.result.text, "90%")

        self.test_result.show_result(self.test_result_failed)
        self.assertEqual(self.test_result.status.text, "Nie zdałeś")
        self.assertEqual(self.test_result.result.text, "20%")


if __name__ == '__main__':
    unittest.main()
