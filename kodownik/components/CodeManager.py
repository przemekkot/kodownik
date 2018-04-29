#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kodownik.components.Code import Code
from kodownik.components.CodeEventDispatcher import code_dispatcher
from kodownik.components.ProductLists import ProductLists
from app_logger import kodlog


class CodeManager:
    products = ProductLists()
    product = None
    code = None

    def __init__(self):
        code_dispatcher.bind(on_number_enter=self.handle_number_enter)
        self.pick_product()

    def pick_product(self):
        self.product = self.products.pick_random()
        self.code = Code(self.product)
        kodlog.info("I picked product: " + self.code.name)
        self.dispatch_product_code()

    def handle_number_enter(self, event, number):
        print(number)
        if self.code.is_next(number):
            self.code.set_user_code(number)
            if self.code.is_equal():
                self.code.is_right = True
        else:
            self.code.is_wrong = True

        code_dispatcher.dispatch_code_event(self.code)

    def dispatch_product_code(self):
        kodlog.info("I dispatched product change")
        code_dispatcher.dispatch_product_event(self.code)