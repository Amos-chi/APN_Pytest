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
        i = 0
        while True:
            try:
                resp = requests.request(method=method,url=url, **kwargs)
                pylogger.alogger.info(f'{method}: {url} - {resp.status_code}')
                break
            except Exception as e :
                print(e)
                i += 1
            finally:
                if i == 5:
                    break

        return resp

if __name__ == '__main__':
    RequestsUtil().request('qweq','sadasdasd')