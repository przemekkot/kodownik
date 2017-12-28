#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import random

# File format:
# Name, type of quantity = (szt, kg), code
# first row is column names
FRUIT_CODES_FILE = "Data/kody_produktow_owoce.csv"
VEGETABLES_CODES_FILE = "Data/kody_produktow_warzywa.csv"
BREAD_CODES_FILE = "Data/kody_produktow_pieczywo.csv"

FRUIT = "fruit"
VEGETABLE = "vegetables"
BREAD = "bread"

class Codes():
    codes_types = [FRUIT, VEGETABLE, BREAD]

    codes_files = {
        FRUIT: FRUIT_CODES_FILE,
        VEGETABLE: VEGETABLES_CODES_FILE,
        BREAD: BREAD_CODES_FILE}

    codes = {
        FRUIT: None,
        VEGETABLE: None,
        BREAD: None}

    def __init__(self):
        self.load_codes()

    def pick_random(self):
        type = self.pick_type()
        return random.choice(self.codes[type])

    def pick_type(self):
        return random.choice(self.codes_types)

    def load_codes(self):
        for type, file in self.codes_files.items():
            csv_file = open(file, newline='')
            codes_list = list(csv.reader(csv_file, delimiter=";"))
            self.codes[type] = codes_list[1:]
        print(self.codes)