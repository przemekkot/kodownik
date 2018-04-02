#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.event import EventDispatcher



class CodeEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_product_change')
        self.register_event_type('on_code_change')
        super(CodeEventDispatcher, self).__init__(**kwargs)

    def dispatch_product_event(self, value):
        print("I dispatch")
        self.dispatch('on_product_change', value)

    def dispatch_code_event(self, value):
        print("I dispatch")
        self.dispatch('on_code_change', value)

    def on_product_change(self, *args):
        pass

    def on_code_change(self, *args):
        pass

code_dispatcher = CodeEventDispatcher()