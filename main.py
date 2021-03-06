#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.config import Config

from kivy.lang import Builder

from kodownik.app.MainApp import MainApp

from app_logger import kodlog

main_kv_file = 'kodownik/kvfiles/main.kv'
app_size = {"width": 800, "height": 900}


if __name__ == "__main__":
    Config.set('graphics', 'width', app_size.get("width"))
    Config.set('graphics', 'height', app_size.get("height"))

    Builder.load_file(main_kv_file)
    app = MainApp()
    app.run()
    kodlog.debug("App is run")
