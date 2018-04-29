#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kodownik.components.Product import EmptyProduct

class Code:
    code = ""
    name = ""
    product = None
    empty = True
    sign_shown = 0
    code_numbers = []
    entered_numbers = []
    highlight_numbers = []
    is_right = False
    is_wrong = False

    def __init__(self, product=EmptyProduct()):
        self.code = product.code
        self.name = product.name
        self.product = product
        self.make_signs()
        self.empty = False

    def make_signs(self):
        self.code_numbers = list(self.code)
        self.code_numbers.reverse()
        self.add_number_to_highlight()
        self.sign_shown = 1

    def is_next(self, number):
        print(self.code_numbers)
        print(self.code_numbers[-1])
        print(number)
        return int(self.code_numbers[-1]) == int(number)

    def is_equal(self):
        return self.code == self.get_user_code()

    def get_user_code(self):
        return "".join(self.entered_numbers)

    def set_user_code(self, number):
        self.entered_numbers.append(number)
        self.sign_shown += 1
        self.add_number_to_highlight()

    def add_number_to_highlight(self):
        if len(self.code_numbers):
            self.highlight_numbers.append(self.code_numbers[-1])

    def get_fraction(self):
        return self.sign_shown / len(self.code)

    def next_sign(self):
        pass
        # self.sign_shown += 1
        # self.next_number = self.code_numbers.pop()
        # return self.next_number

    def is_code_right(self, entered_code):
        return self.code == entered_code

    def reset_code(self):
        self.make_signs()