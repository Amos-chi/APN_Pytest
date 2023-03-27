# Time : 2023/3/10 14:15
import datetime

import pytest

from common.requests_util import RequestsUtil
from common.yaml_util import get_Auth
from testcases.B端.批量创建job.临时调试 import readaslist
from testcases.B端.批量创建job.循环创建job_B端 import test_create_nyfs, test_create_jobs

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

class TestBclient():

    '''
        B端创建jobs, 为了避免资源占用把传参方法注释了, 用时打开
    '''

    @pytest.mark.Bclient
    def test_createJobs(self):

        i = 1
        while datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'), '%Y-%m-%d  %H:%M:%S') \
                < datetime.datetime.strptime("2023-03-17T14:00:00Z", '%Y-%m-%dT%H:%M:%SZ'):
            data = test_create_nyfs(i)

            try:
                num = test_create_jobs(data)
                if num == 1:
                    i += 1
                else:
                    pass

            except Exception as e:
                print(e)