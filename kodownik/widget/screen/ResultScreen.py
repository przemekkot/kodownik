#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.gridlayout import GridLayout

from kodownik.widget.test_result import TestResult

NUMBER_OF_TEST_CODES=20

class ResultScreen(GridLayout):
    test_result = TestResult(cols=1, rows=2)
    codes_list = Codes_List(cols=1, rows=NUMBER_OF_TEST_CODES)
