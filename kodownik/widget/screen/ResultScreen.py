#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.gridlayout import GridLayout

from kodownik.widget.CodesList import CodesList
from kodownik.widget.TestResult import TestResult

from kodownik.widget.button.ResultButtons import ResultButtons

NUMBER_OF_TEST_CODES=20

class ResultScreen(GridLayout):
    test_result = TestResult(cols=1, rows=2)
    codes_list = CodesList(cols=1, rows=NUMBER_OF_TEST_CODES)
    result_buttons = ResultButtons(cols=2, rows=1)