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

    data_dict = read_yamlfile('\\hotdata\\company\\company_list_new.yaml')

    @pytest.mark.company
    @pytest.mark.parametrize('param',data_dict)
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
                            if assertKey in ['active', 'level', 'name', 'country', 'industry']:
                                for i in resp.json():
                                    assert assertValue == i[assertKey]

                            else:
                                print('错误断言类型!')
                                assert False

                elif key in ['contain','ct']:
                    for assertKey, assertValue in value.items():
                        if assertKey == 'accountManagers':
                            for i in resp.json():
                                namelist = []
                                for am in i['accountManager']:
                                    namelist.append(am['fullName'])
                                namelist_str = ','.join(namelist)
                                assert assertValue in namelist_str

                        elif assertKey == 'companyName':
                            for i in resp.json():
                                assert assertValue in i['name']

                elif key in ['gt', 'great_than', 'bigger_than']:
                    print('不是相等断言 另外处理')

                elif key in ['lt', 'less']:
                    print('不是相等断言 另外处理')

