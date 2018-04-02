import unittest
# FunctionTestCase
# my_function

class FunctionTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_my_function(self):
        self.assertTrue(my_function())



if __name__ == '__main__':
    unittest.main()
