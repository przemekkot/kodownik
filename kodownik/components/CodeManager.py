#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kodownik.components.Code import Code
from kodownik.components.WorkflowEventDispatcher import event_dispatcher
from kodownik.components.ProductLists import ProductLists
from app_logger import kodlog


class CodeManager:
    products = ProductLists()
    product = None
    code = None

    def __init__(self):
        self.pick_product()

    def pick_product(self):
        self.product = self.products.pick_random()
        self.code = Code(self.product)
        kodlog.info("I picked product: " + self.code.name)
        return self.code