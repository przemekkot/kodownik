import unittest
# TestResultTestCase
# if_is
from kivy.uix.label import Label

from kodownik.widget.test_result import TestResult


class TestResultTestCase(unittest.TestCase):
    def setUp(self):
        self.test_result = TestResult()

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

if __name__ == '__main__':
    unittest.main()
