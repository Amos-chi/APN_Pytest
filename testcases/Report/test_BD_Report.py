import pytest
from pytest_assume.plugin import assume
from common.requests_util import RequestsUtil
from common.yaml_util import read_yamlfile, get_Auth
import json
proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }


class TestCompany_clientlist():
    pass
    # @pytest.mark.company
    # @pytest.mark.parametrize('param',read_yamlfile('\\hotdata\\new_yaml_files\\company_list_nyf.yaml'))
    # def test_clientlist(self,param):
    #     print(param['feature']+ '.' +param['story']+ '.' +param['title'])
    #     url = param['requests']['url']
    #     data = param['requests']['data']
    #     headers = {'Authorization': get_Auth('Authorization')}
    #     method = param['requests']['method']
    #     resp = RequestsUtil().request(method=method, url=url, json=data, headers=headers, proxies=proxies)
    #     for i in param['validate']:
    #         print(i)

