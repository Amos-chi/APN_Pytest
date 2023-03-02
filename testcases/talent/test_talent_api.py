import json

import pytest

from common.assert_util import get_extract, assert_
from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from common.yaml_util import read_yamlfile, get_Auth
from testcases.talent.conftest import pre

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }



class TestCompany_clientlist():

    @pytest.mark.talent
    @pytest.mark.parametrize('param',pre()['talnet_moduleTest'])
    def test_clientlist(self,param):
        # 显示测试模块 - 用例 - 测试项
        pylogger.alogger.info(f" ---> 测试用例: {param['feature']}. {param['story']}. {param['title']}")
        url = param['requests']['url']
        data = param['requests']['data']
        headers = {'Authorization': get_Auth('Authorization')}
        method = param['requests']['method']
        resp = RequestsUtil().request(method=method, url=url, json=data, headers=headers, proxies=proxies)
        if resp.status_code in [200,201]:
            if type(resp.json()) is list:
                pylogger.alogger.info(f'{len(resp.json())} results: ')
                n = 1
                for i in resp.json():
                    pylogger.alogger.info(f'第 {n} 个结果: ')
                    res_dict = get_extract(i, param)    # 对每个公司, 获取要断言的字段 , 返回一个字典
                    assert_(res_dict,param)     # 把返回的字典, 和断言规则一起传给assert_方法 进行断言比较
                    n += 1
            if type(resp.json()) is dict:
                res_dict = get_extract(resp.json(), param)
                assert_(res_dict, param)
        else:
            assert resp.status_code == 200



