import os

import pytest

from common.Pre import pre
from common.logger_util import pylogger

module = 'talent'

@pytest.fixture(scope='package', autouse=True)
def set_log():
    pylogger.alogger.info('{:-^50}'.format(f' 开始测试 {module} 模块 '))

def prepare():
    data_dict = pre(module)
    return data_dict

def pre_createbyresume():
    list_ = []
    resumePath = r'E:\Parser_Test\resume_files'
    files = os.listdir(resumePath)
    for file in files:
        list_.append((resumePath,file))
    return list_