#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.event import EventDispatcher

from app_logger import kodlog


class WorkflowEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_pick_a_product')
        self.register_event_type('on_show_product')
        self.register_event_type('on_handle_user_enter_number')
        self.register_event_type('on_show_next_number')
        self.register_event_type('on_handle_user_submit_code')
        super(WorkflowEventDispatcher, self).__init__(**kwargs)

    def do_pick_a_product(self):
        kodlog.info("I pick a product")
        self.dispatch('on_pick_a_product')

    def do_show_product(self, code=None):
        kodlog.info("I show product")
        self.dispatch('on_show_product', code)

    def do_handle_user_enter_number(self, value):
        kodlog.info("I handle user enter number")
        self.dispatch('on_handle_user_enter_number', value)

    def do_show_next_number(self, value):
        kodlog.info("I show next number")
        self.dispatch('on_show_next_number', value)

    def do_handle_user_submit_code(self, value):
        kodlog.info("I handle user submit code")
        self.dispatch('on_handle_user_submit_code', value)

    def on_pick_a_product(self, *args):
        pass

    def on_show_product(self, *args):
        pass

    def on_handle_user_enter_number(self, *args):
        pass

    def on_show_next_number(self, *args):
        pass

    def on_handle_user_submit_code(self, *args):
        pass

event_dispatcher = WorkflowEventDispatcher()