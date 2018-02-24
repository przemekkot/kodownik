#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Code:
    name = None
    code = None
    quantity_type = None

    def __init__(self, code):
        self.name = code[0]
        self.code = code[2]
        self.quantity_type = code[1]