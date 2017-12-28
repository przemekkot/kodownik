#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CodePresenter:
    code = ""
    code_signs = []
    empty = True

    def __init__(self, code=""):
        self.code = code
        self.code_signs = list(code)
        self.code_signs.reverse()
        self.empty = False

    def next_sign(self):
        return self.code_signs.pop()