import json

import pytest

from common.assert_util import get_extract, assert_
from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from common.yaml_util import read_yamlfile, get_Auth
from testcases.Companies.conftest import pre

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }


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
        resp = RequestsUtil().request(method=method, url=url, json=data, headers=headers, proxies=proxies)
        if resp.status_code == 200:
            pylogger.alogger.info(f'{len(resp.json())} results: ')
            #print(f'resp.json: {json.dumps(resp.json(),indent=4)}')
            n = 1
            for i in resp.json():
                pylogger.alogger.info(f'第 {n} 个结果: ')
                # 对每个公司, 获取要断言的字段 , 返回一个字典
                res_dict = get_extract(i, param)
                #print(res_dict)
                # 把返回的字典, 和断言规则一起传给assert_方法 进行断言比较
                assert_(res_dict,param)
                n += 1
        else:
            assert resp.status_code == 200





        # for i in param['validate']:
        #     print(i)
        #     for key, value in i.items():
        #         if key in ['eq', 'equal', 'equals']:
        #             for assertKey, assertValue in value.items():
        #                 if assertKey == 'status_code':
        #                     print(f'{assertKey}: {getattr(resp,assertKey)}')
        #                     assert assertValue == getattr(resp,assertKey)
        #                 else:
        #                     if assertKey in ['active', 'level', 'name', 'country', 'industry']:
        #                         for i in resp.json():
        #                             assert assertValue == i[assertKey]
        #
        #                     else:
        #                         print('错误断言类型!')
        #                         assert False
        #
        #         elif key in ['contain','ct']:
        #             for assertKey, assertValue in value.items():
        #                 if assertKey == 'accountManagers':
        #                     for i in resp.json():
        #                         namelist = []
        #                         for am in i['accountManager']:
        #                             namelist.append(am['fullName'])
        #                         namelist_str = ','.join(namelist)
        #                         assert assertValue in namelist_str
        #
        #                 elif assertKey == 'companyName':
        #                     for i in resp.json():
        #                         assert assertValue in i['name']
        #
        #         elif key in ['gt', 'great_than', 'bigger_than']:
        #             print('不是相等断言 另外处理')
        #
        #         elif key in ['lt', 'less']:
        #             print('不是相等断言 另外处理')

