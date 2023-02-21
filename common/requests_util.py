# Time : 2023/2/11 15:40

import requests
from common.logger_util import pylogger
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
class RequestsUtil():

    def request(self,method,url,**kwargs):
        method = str(method).lower()
        while True:
            try:
                resp = requests.request(method=method,url=url, **kwargs)
                pylogger.alogger.info(f'{method}: {url} - {resp.status_code}')
                break
            except Exception as e :
                print(e)

        return resp