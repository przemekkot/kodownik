import unittest
# CodesList
# if_is
from kivy.uix.gridlayout import GridLayout

from kodownik.widget.CodesList import CodesList


class CodesListTestCase(unittest.TestCase):
    def setUp(self):
        self.codes_list = CodesList()

    def tearDown(self):
        pass

    def test_if_is(self):
        self.assertTrue(self.codes_list)
        self.assertIsInstance(self.codes_list, GridLayout)



if __name__ == '__main__':
    unittest.main()
