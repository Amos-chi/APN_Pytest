import json

import pytest

from common.requests_util import RequestsUtil
from testcases.talent.conftest import prepare

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }



class TestTalent():

    '''
        创建候选人接口
    '''
    @pytest.mark.talent
    @pytest.mark.parametrize('param',prepare()['talnet_moduleTest'])
    def test_talnet_moduleTest(self,param,base_url):
        RequestsUtil().normal_apis(param,base_url)




