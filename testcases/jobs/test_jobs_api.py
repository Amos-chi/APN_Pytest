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
        生成模板文件时 会用今天的日期作为文件夹名, 调用readaslist()方法时, 需要传一个今天的日期
         a. : 准备数据
         b. : 修改readaslist()方法中的日期
         
         c. : 为了避免每次启动都准备100个job传参, 注释掉了传参夹具, 使用时打开
    '''
    @pytest.mark.runn
    #@pytest.mark.parametrize('param', readaslist('2023-03-15'))
    def test_create_jobs(self,param):
        url = 'https://api-staging.hitalentech.com:8888/job/api/v3/jobs'
        data = param
        headers = {'Authorization': get_Auth('Authorization')}
        method = 'post'
        try:
            params = param['requests']['params']
        except:
            params = None
        resp = RequestsUtil().request(method=method, url=url, json=data, params=params, headers=headers,
                                      proxies=proxies)
        pylogger.alogger.info(resp.json())



