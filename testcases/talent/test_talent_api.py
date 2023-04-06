import datetime
import json
import os

import pytest

from common.requests_util import RequestsUtil
from testcases.talent.V3_parser.formatParserResult import createbyresume
from testcases.talent.conftest import prepare, pre_createbyresume

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }



class TestTalent():

    '''
        创建候选人接口
        读取csv 批量创建候选人
        需要先运行 修改电话邮箱.py 让每个用例的数据为随机值
    '''
    @pytest.mark.talent
    @pytest.mark.parametrize('param',prepare()['talnet_moduleTest'])
    def test_createWithoutResumes(self,param,base_url):
        RequestsUtil().normal_apis(param,base_url)

    '''
        批量上传简历创建候选人
    '''


    @pytest.mark.talent
    @pytest.mark.parametrize('pairs', pre_createbyresume())
    def test_createByResumes(self, pairs):
        # 以日为单位 创建文件夹存放结果json
        date_ = datetime.datetime.now().strftime('%Y-%m-%d')
        date_dir = './testcases/talent/V3_parser/results_history' + '/' + date_
        if not os.path.exists(date_dir):
            os.makedirs(date_dir)

        resumePath = pairs[0]
        files = pairs[1]
        # 创建
        createbyresume(resumePath, files, date_dir)


