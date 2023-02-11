import pytest

from common.requests_util import RequestsUtil
from common.yaml_util import read_yaml, read_yamlfile

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }


class TestCompany_clientlist():

    @pytest.mark.company
    @pytest.mark.parametrize('param',read_yamlfile('\\testcases\\Companies\\company_list.yml'))
    def test_clientlist(self,param):
        print(param['feature']+param['story']+param['title'])
        url = param['requests']['url']
        json = param['requests']['data']
        headers = {'Authorization': read_yaml('Authorization')}
        method = param['requests']['method']
        resp = RequestsUtil().request(method=method, url=url, json=json, headers=headers, proxies=proxies)
        print(param['validate'])



