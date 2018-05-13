#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.properties import VariableListProperty
from kivy.uix.gridlayout import GridLayout

from app_logger import kodlog
from kodownik.components.LearningWorkflow import LearningWorkflow
from kodownik.components.WorkflowEventDispatcher import event_dispatcher
from kodownik.components.CodeManager import CodeManager
from kodownik.widget.button.AppButtons import AppButtons
from kodownik.widget.label.ProductCode import ProductCode
from kodownik.widget.label.ProductName import ProductName
from kodownik.widget.ScreenKeyboard import ScreenKeyboard
from kodownik.widget.button.SubmitButtons import SubmitButtons


class CodeScreen(GridLayout):
    padding = VariableListProperty(100)
    spacing = VariableListProperty(10, length=2)
    code_manager = CodeManager()

    product_name = ProductName()
    product_code = ProductCode()
    screen_keyboard = ScreenKeyboard(cols=1, rows=1)
    submit_buttons = SubmitButtons(cols=2, rows=1, size_hint=(1, .3))
    app_buttons = AppButtons(cols=2, rows=1, size_hint=(1, .3))

    def __init__(self, **kwargs):
        super(CodeScreen, self).__init__(**kwargs)

        self.add_widget(self.product_code)
        self.add_widget(self.screen_keyboard)
        self.add_widget(self.submit_buttons)
        self.add_widget(self.product_name)
        self.add_widget(self.app_buttons)

        self.learning = LearningWorkflow(
            cm=self.code_manager,
            product_code=self.product_code,
            product_name=self.product_name,
            screen_keyboard=self.screen_keyboard,
            submit_buttons=self.submit_buttons
        )
        self.begin_learning()

    def begin_learning(self):
        kodlog.info("I started showing codes")
        event_dispatcher.do_pick_a_product()