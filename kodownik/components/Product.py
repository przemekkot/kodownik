#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Product:
    name = None
    code = None
    quantity_type = None

    def __init__(self, code, name = None, quantity_type = None):
        if type(code) is list:
            self.name = code[0]
            self.code = code[2]
            self.quantity_type = code[1]
        else:
            self.name = name
            self.code = code
            self.quantity_type = quantity_type




class EmptyProduct(Product):
    def __init__(self):
        super(EmptyProduct, self).__init__(["Brak produktu", "szt", ""])