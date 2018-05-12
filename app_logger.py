#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

from os import path

logger_conf = path.dirname(__file__) + "/logging.conf"
logging.config.fileConfig(logger_conf)
#logging.basicConfig(filename='run.log', level=logging.DEBUG)
kodlog = logging.getLogger(__name__)
kodlog.info("test message")

