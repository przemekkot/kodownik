#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class ResultWidget(GridLayout):

    def __init__(self, **kwargs):
        super(ResultWidget, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 3
        self.passed = False
        self.name = Label()
        self.proper_code = Label()
        self.entered_code = Label()
    def show_result(self, result):
        """

        :param result:
        :type result: tuple
        :return:
        """
        self.passed = result[2]
        self.name.text = result[0].name
        self.proper_code.text = result[0].code
        self.entered_code.text = result[1].code


class CodesList(GridLayout):

    def __init__(self, count=10, **kwargs):
        super(CodesList, self).__init__(**kwargs)
        self.ammount_of_codes = count
        self.make_list(count)

    def make_list(self, ammount_of_codes):
        self.label_list = [ResultWidget() for i in range(ammount_of_codes)]

    def show_results(self, results):
        """

        :param results:
        :type results: tuple
        :return:
        """
        if len(results) != self.ammount_of_codes:
            raise IndexError

        for _index, result in enumerate(results):
            widget = self.label_list[_index]
            widget.show_result(result)
