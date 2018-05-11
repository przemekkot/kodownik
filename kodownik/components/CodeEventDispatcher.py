#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.event import EventDispatcher

class CodeEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_product_change')
        self.register_event_type('on_code_change')
        self.register_event_type('on_next_product')
        self.register_event_type('on_submit_code')
        self.register_event_type('on_test_finished')
        super(CodeEventDispatcher, self).__init__(**kwargs)

    def dispatch_product_event(self, value):
        print("I dispatch")
        self.dispatch('on_product_change', value)

    def dispatch_code_event(self, value):
        print("I dispatch")
        self.dispatch('on_code_change', value)

    def dispatch_next_product_event(self, value):
        self.dispatch('on_next_product', value)

    def dispatch_submit_code_event(self, value):
        self.dispatch('on_submit_code', value)

    def dispatch_test_finished_event(self, value):
        self.dispatch('on_test_finished', value)

    def on_product_change(self, *args):
        pass

    def on_code_change(self, *args):
        pass

    def on_next_product(self, *args):
        pass

    def on_submit_code(self, *args):
        pass

    def on_test_finished(self, *args):
        pass

code_dispatcher = CodeEventDispatcher()