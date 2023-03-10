# Time : 2023/3/10 14:15
import pytest

from common.requests_util import RequestsUtil
from common.yaml_util import get_Auth
from testcases.B端.批量创建job.临时调试 import readaslist

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

class TestBclient():

    @pytest.mark.Bclient
    @pytest.mark.parametrize('param', readaslist())
    def test_createJobs(self,param):
        url = 'https://api-staging.hitalentech.com:8443/apnpublic/api/v1/biz/jobs/'
        data = param
        headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsicmVzX2FwaSJdLCJ1c2VyX25hbWUiOiJ7XCJhY3RpdmF0ZWRcIjp0cnVlLFwiZW1haWxcIjpcImlwZ0BhbHRvbW5pLmNvbVwiLFwiZmlyc3ROYW1lXCI6XCJJUEdcIixcImlkXCI6NCxcImxhc3ROYW1lXCI6XCJHcm91cFwiLFwidGVuYW50SWRcIjo2NjYwMDA0LFwidWlkXCI6XCI0LDY2NjAwMDRcIixcInVzZXJuYW1lXCI6XCJmZGJhZDk4MGQwZjcxMDc1MzcxYjFkYjBiNWIxOTNjM1wifSIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2Nzg0MzQwMTEsImF1dGhvcml0aWVzIjpbIlJPTEVfQURNSU4iLCJST0xFX1VTRVIiXSwianRpIjoiNGMyZDRkNTYtNDk2MC00MTZkLWIzMmItODFlZTk4ZGNkODA5IiwiY2xpZW50X2lkIjoiYXBucHVibGljYXBwIn0.blvMplfDVRcpnSFSUM7whhQcQfhEUBMr-yeNh0Vs_ac'}
        method = 'post'
        try:
            params = param['requests']['params']
        except:
            params = None
        resp = RequestsUtil().request(method=method, url=url, json=data, params=params, headers=headers,
                                      proxies=proxies)
        print(resp.json())
