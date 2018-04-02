#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Product:
    name = None
    code = None
    quantity_type = None

    def __init__(self, code):
        self.name = code[0]
        self.code = code[2]
        self.quantity_type = code[1]

class EmptyProduct(Product):
    def __init__(self):
        super(EmptyProduct, self).__init__(["Brak produktu", "szt", ""])