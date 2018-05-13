#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kodownik.components.Product import EmptyProduct

class Code:
    code = ""
    name = ""
    product = None
    buttons_to_press = []
    highlight_number = None

    def __init__(self, product=EmptyProduct()):
        self.code = product.code
        self.name = product.name
        self.quantity = product.quantity_type
        self.product = product
        self.buttons_to_press = list(self.code)
        self.highlight_number = self.get_first_number()

    def __eq__(self, other):
        return self.code == other.code

    def get_next_number(self):
        self.highlight_number = self.get_first_number()

    def get_first_number(self):
        if len(self.buttons_to_press) == 0:
            return None

        return self.buttons_to_press.pop(0)
