#!/usr/bin/env python3
# -*- encoding=utf8 -*-

########################################################################
# Created time: 2024-08-27 18:03:44
# Author: Jason Young (杨郑鑫).
# E-Mail: AI.Jason.Young@outlook.com
# Last Modified by: Jason Young (杨郑鑫)
# Last Modified time: 2024-12-31 16:09:37
# Copyright (c) 2024 Yangs.AI
# 
# This source code is licensed under the Apache License 2.0 found in the
# LICENSE file in the root directory of this source tree.
########################################################################


from . import dataset
from . import modules
from . import commons

import importlib.metadata

from younger.commons.constants import YoungerHandle


__version__ = importlib.metadata.version("younger_logics_ir")


__thename__ = YoungerHandle.LogicsName + '-' + 'IR'
