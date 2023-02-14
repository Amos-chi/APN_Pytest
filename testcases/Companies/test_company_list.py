import pytest

from common.requests_util import RequestsUtil
from common.yaml_util import read_yamlfile, get_Auth
import json
proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }


class TestCompany_clientlist():

    @pytest.mark.company
    @pytest.mark.parametrize('param',read_yamlfile('\\hotdata\\new_yaml_files\\nyf.yaml'))
    def test_clientlist(self,param):
        print(param['feature']+ '.' +param['story']+ '.' +param['title'])
        url = param['requests']['url']
        data = param['requests']['data']
        headers = {'Authorization': get_Auth('Authorization')}
        method = param['requests']['method']
        resp = RequestsUtil().request(method=method, url=url, json=data, headers=headers, proxies=proxies)
        for i in param['validate']:
            print(i)
            for key, value in i.items():
                if key in ['eq', 'equal', 'equals']:
                    for assertKey, assertValue in value.items():
                        if assertKey == 'status_code':
                            print(f'{assertKey}: {getattr(resp,assertKey)}')
                            assert assertValue == getattr(resp,assertKey)
                        else:
                            print(f'{assertKey}: {resp.json()[assertKey]}')
                            assert assertValue == resp.json()[assertKey]
                else:
                    print('不是相等断言 另外处理')

