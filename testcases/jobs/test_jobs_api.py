import json

import pytest

from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from common.yaml_util import read_yamlfile, get_Auth
from testcases.jobs.conftest import prepare
from testcases.jobs.批量创建.生成nyf文件 import readaslist

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

    '''
        大量创建job
        用模板先批量生成了yaml传参文件, 读成一个list传到parametrize
    '''
    # @pytest.mark.parametrize('param', readaslist())
    # def test_create_jobs(self,param):
    #     url = 'https://api-staging.hitalentech.com:8888/job/api/v3/jobs'
    #     data = param
    #     headers = {'Authorization': get_Auth('Authorization')}
    #     method = 'post'
    #     try:
    #         params = param['requests']['params']
    #     except:
    #         params = None
    #     resp = RequestsUtil().request(method=method, url=url, json=data, params=params, headers=headers,
    #                                   proxies=proxies)
    #     print(resp.status_code)
    #     print(resp.json())


