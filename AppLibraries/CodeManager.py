#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import ObjectProperty

from AppLibraries.Code import Code
from AppLibraries.ProductLists import ProductLists
from AppLibraries.CodeEventDispatcher import code_dispatcher

class CodeManager:
    products = ProductLists()
    product = None
    code = None

    def __init__(self):
        self.pick_product()

    def pick_product(self):
        self.product = self.products.pick_random()
        self.code = Code(self.product)
        print("I will dispatch")
        code_dispatcher.dispatch_code_event(self.code)