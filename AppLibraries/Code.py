#!/usr/bin/env python
# -*- coding: utf-8 -*-
from AppLibraries.Product import EmptyProduct


class Code:
    code = ""
    name = ""
    product = None
    empty = True
    sign_shown = 0
    code_signs = []

    def __init__(self, product=EmptyProduct()):
        self.code = product.code
        self.name = product.name
        self.product = product
        self.make_signs()
        self.empty = False

    def make_signs(self):
        self.code_signs = list(self.code)
        self.code_signs.reverse()
        self.sign_shown = 1

    def get_fraction(self):
        return self.sign_shown / len(self.code)

    def next_sign(self):
        self.sign_shown += 1
        return self.code_signs.pop()

    def is_code_right(self, entered_code):
        return self.code == entered_code

    def reset_code(self):
        self.make_signs()