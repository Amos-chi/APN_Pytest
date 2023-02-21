# Time : 2023/2/10 11:20
from common.logger_util import pylogger
from common.yaml_util import set_Auth, get_Auth
from common.requests_util import RequestsUtil


class GetAuthorization:

    proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }
    def get_Authorization(self):
        pylogger.alogger.info('{:-^50}'.format('运行了get_Authorization'))

        url= 'https://api-staging.hitalentech.com:8888/user/api/v3/login'
        data = {
            'username' : 'amos.chi',
            'password' : 'a123456'
        }
        #resp = requests.post(url=url, json=data, proxies=GetAuthorization.proxies)
        resp = RequestsUtil().request(method='post', url=url, json=data, proxies=GetAuthorization.proxies)
        token = resp.json()['credential']['access_token']
        Authorization = 'Bearer ' + token
        set_Auth({'Authorization': Authorization})

if __name__ == '__main__':
    GetAuthorization().get_Authorization()
    print(get_Auth('Authorization'))