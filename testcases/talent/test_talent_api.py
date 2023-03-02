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



class TestTalent():

    '''
        创建候选人接口
    '''
    @pytest.mark.talent
    @pytest.mark.parametrize('param',pre()['talnet_moduleTest'])
    def test_talnet_moduleTest(self,param):
        RequestsUtil().normal_apis(param)



