import json

import pytest

from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from common.yaml_util import read_yamlfile, get_Auth
from testcases.company.conftest import prepare

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

'''
@pytest.mark.parametrize 函数传值 取的是对应csv的文件名[:-4]
'''
class TestCompany():

    '''
        获取company列表
    '''
    @pytest.mark.company
    @pytest.mark.parametrize('param',prepare()['company_list'])
    def test_clientlist(self,param,base_url):
        RequestsUtil().normal_apis(param,base_url)


    '''
        获取没合同的公司
    '''
    @pytest.mark.runn
    @pytest.mark.company
    def test_noContract_Clients1(self,base_url):
        url = f'{base_url}/company/api/v3/company/noContracts'
        headers = {'Authorization': get_Auth('Authorization')}
        resp = RequestsUtil().request('get', url=url, headers=headers, proxies=proxies)
        pylogger.alogger.info(f'Num of No Contract CLients: {len(resp.json())}')
        assert resp.status_code == 200


