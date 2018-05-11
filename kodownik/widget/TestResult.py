#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

_result_passed = "Zdałeś"
_result_failed = "Nie zdałeś"

class TestResult(GridLayout):

    def __init__(self, **kwargs):
        super(TestResult, self).__init__(**kwargs)
        self.add_labels()

    def add_labels(self):
        """ Add labels """
        self.status = Label()
        self.result = Label()

        self.add_widget(self.status)
        self.add_widget(self.result)

    def show_result(self, test):
        """
        test = {
            'passed' : False,
            'result' : "20%"
        }

        :param test:
        :type test: dict
        """
        if test['passed']:
            self.status.text = _result_passed
        else:
            self.status.text = _result_failed
        self.result.text = test['result']