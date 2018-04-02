#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import random

# File format:
# Name, type of quantity = (szt, kg), code
# first row is column names
from kodownik.components.Product import Product

FRUIT_PRODUCTS_FILE = "kodownik/data/kody_produktow_owoce.csv"
VEGETABLES_PRODUCTS_FILE = "kodownik/data/kody_produktow_warzywa.csv"
BREAD_PRODUCTS_FILE = "kodownik/data/kody_produktow_pieczywo.csv"

FRUIT = "fruit"
VEGETABLE = "vegetables"
BREAD = "bread"

class ProductLists():
    product_types = [FRUIT, VEGETABLE, BREAD]

    product_files = {
        FRUIT: FRUIT_PRODUCTS_FILE,
        VEGETABLE: VEGETABLES_PRODUCTS_FILE,
        BREAD: BREAD_PRODUCTS_FILE}

    products = {
        FRUIT: None,
        VEGETABLE: None,
        BREAD: None}

    def __init__(self):
        self.load_products()

    def pick_random(self):
        type = self.pick_type()
        return Product(random.choice(self.products[type]))

    def pick_type(self):
        return random.choice(self.product_types)

    def load_products(self):
        for type, file in self.product_files.items():
            csv_file = open(file, newline='')
            loaded_products = list(csv.reader(csv_file, delimiter=";"))
            filtered_products = self.filter(loaded_products)
            self.products[type] = filtered_products[1:]

    def filter(self, products):
        return list(filter(lambda row: len(row[2]) < 5, products ))