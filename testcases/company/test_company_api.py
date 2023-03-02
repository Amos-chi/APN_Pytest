import json

import pytest

from common.assert_util import get_extract, assert_
from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from common.yaml_util import read_yamlfile, get_Auth
from testcases.company.conftest import pre

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

'''
@pytest.mark.parametrize 函数传值 取的是对应csv的文件名[:-4]
'''
class TestCompany_clientlist():

    @pytest.mark.company
    @pytest.mark.parametrize('param',pre()['company_list'])
    def test_clientlist(self,param):
        # 显示测试模块 - 用例 - 测试项
        pylogger.alogger.info(f" ---> 测试用例: {param['feature']}. {param['story']}. {param['title']}")
        url = param['requests']['url']
        data = param['requests']['data']
        headers = {'Authorization': get_Auth('Authorization')}
        method = param['requests']['method']
        params = param['requests']['params']
        resp = RequestsUtil().request(method=method, url=url, json=data, params=params, headers=headers, proxies=proxies)
        if resp.status_code in [200, 201]:
            if type(resp.json()) is list:
                pylogger.alogger.info(f'{len(resp.json())} results: ')
                n = 1
                for i in resp.json():
                    pylogger.alogger.info(f'第 {n} 个结果: ')
                    res_dict = get_extract(i, param)  # 对每个公司, 获取要断言的字段 , 返回一个字典
                    assert_(res_dict, param)  # 把返回的字典, 和断言规则一起传给assert_方法 进行断言比较
                    n += 1
            if type(resp.json()) is dict:
                res_dict = get_extract(resp.json(), param)
                assert_(res_dict, param)
        else:
            assert resp.status_code == 200


    @pytest.mark.test
    @pytest.mark.company
    def test_noContract_Clients1(self,base_url):
        url = f'{base_url}/company/api/v3/company/noContracts'
        print(url)
        headers = {'Authorization': get_Auth('Authorization')}
        resp = RequestsUtil().request('get', url=url, headers=headers, proxies=proxies)
        pylogger.alogger.info(f'Num of No Contract CLients: {len(resp.json())}')
        assert resp.status_code == 200


