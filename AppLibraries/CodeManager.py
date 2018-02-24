#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import ObjectProperty

from AppLibraries.CodeLists import CodeLists


class CodeManager:
    code_lists = CodeLists()
    picked_code = None

    def __init__(self):
        self.picked_code = self.code_lists.pick_random()