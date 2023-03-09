import json

import pytest

from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from common.yaml_util import read_yamlfile, get_Auth
from testcases.jobs.conftest import prepare

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

'''
@pytest.mark.parametrize 函数传值 取的是对应csv的文件名[:-4]
'''
class TestJobs():

    '''
        获取jobs列表
    '''
    @pytest.mark.jobs
    @pytest.mark.parametrize('param',prepare()['job_list'])
    def test_joblist(self,param,base_url):
        RequestsUtil().normal_apis(param,base_url)




