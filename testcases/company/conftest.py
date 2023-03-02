#@pytest.fixture(scope='session',autouse=True)
import os

import chardet
import codecs
import csv
import re
import time
from contextlib import ExitStack

from common.Pre import pre
from common.yaml_util import read_yamlfile
import pytest

from common.logger_util import pylogger


module = 'company'

@pytest.fixture(scope='package', autouse=True)
def set_log():
    pylogger.alogger.info('{:-^50}'.format(f' 开始测试 {module} 模块 '))

def prepare():
    data_dict = pre(module)
    return data_dict