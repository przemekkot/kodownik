#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

logging.config.fileConfig('logging.conf')
#logging.basicConfig(filename='run.log', level=logging.DEBUG)
kodlog = logging.getLogger(__name__)
kodlog.info("test message")

