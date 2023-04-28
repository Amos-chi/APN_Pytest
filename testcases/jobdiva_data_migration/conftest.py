#@pytest.fixture(scope='session',autouse=True)
import os

from pymongo import MongoClient

from common.Pre import pre
import pytest

from common.logger_util import pylogger
from 单独任务.数据库.jobdiva数据迁移1.MongoDB import jobdiva_connection

module = 'jobdiva数据迁移'

@pytest.fixture(scope='package', autouse=True)
def set_log():
    pylogger.alogger.info('{:-^50}'.format(f' 开始测试 {module} 模块 '))


def get_companies():

    db = jobdiva_connection()
    companyNames = ['Google']

    return db,companyNames