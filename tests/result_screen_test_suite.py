#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from tests.test_codes_list import CodesListTestCase
from tests.test_result_buttons import ResultButtonsTestCase
from tests.test_result_screen import ResultScreenTestCase
from tests.test_test_result import TestResultTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestResultTestCase))
    suite.addTest(unittest.makeSuite(CodesListTestCase))
    suite.addTest(unittest.makeSuite(ResultButtonsTestCase))
    suite.addTest(unittest.makeSuite(ResultScreenTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())