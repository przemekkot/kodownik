#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv


# File format:
# Name, type of quantity = (szt, kg), code
# first row is column names
import random


class Codes():

    def __init__(self, file):
        csv_file = open(file, newline='')
        codes_list= list(csv.reader(csv_file, delimiter=";"))
        self.codes_list = codes_list[1:]
        csv_file.close()

    def pick_one(self):
        return self.codes_list.pop()

    def pick_random(self):
        return random.choice(self.codes_list)