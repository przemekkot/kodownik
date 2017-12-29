#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CodePresenter:
    code = ""
    code_signs = []
    empty = True
    sign_shown = 0

    def __init__(self, code=""):
        self.code = code
        self.make_signs(code)
        self.empty = False

    def make_signs(self, code):
        self.code_signs = list(code)
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
        self.make_signs(self.code)