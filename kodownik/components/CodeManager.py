#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import ObjectProperty

from kodownik.components.Code import Code
from kodownik.components.CodeEventDispatcher import code_dispatcher
from kodownik.components.ProductLists import ProductLists


class CodeManager:
    products = ProductLists()
    product = None
    code = None

    def __init__(self):
        self.pick_product()

    def pick_product(self):
        self.product = self.products.pick_random()
        self.code = Code(self.product)
        self.dispatch_product_code()

    def dispatch_product_code(self):
        print("I will dispatch")
        code_dispatcher.dispatch_product_event(self.code)