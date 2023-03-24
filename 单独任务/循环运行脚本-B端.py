# Time : 2023/3/15 9:50
import datetime
import json
import os
import random
import time

import requests
import yaml

from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from testcases.B端.批量创建job.enums import jf, skills, type_

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

#登录方法
def login():
    url = 'https://api-staging.hitalentech.com:8443/apnpublic/api/v1/biz/users/login'
    data = {
        'email': 'ipg@altomni.com',
        'password': 'Ipg123456'
    }
    resp = requests.post(url=url, json=data, proxies=proxies)
    token = resp.json()['credential']['access_token']
    Authorization = 'Bearer ' + token

    f = open('../testcases/B端/Authorization.yaml', 'w', encoding='utf-8')
    yaml.dump({'Authorization': Authorization},stream=f,allow_unicode=True)

def get_token():
    f = open('../testcases/B端/Authorization.yaml', 'r', encoding='utf-8')
    token = yaml.load(stream=f, Loader=yaml.FullLoader)
    return token



def test_create_nyfs(i):
    date_ = datetime.datetime.now().strftime('%Y-%m-%d')
    date_dir = f'../testcases/B端/批量创建job/测试es同步/{date_}'
    if not os.path.exists(date_dir):
        os.makedirs(date_dir)

    f = open('../testcases/B端/批量创建job/传参模板.json', 'r', encoding='utf-8')
    data = json.load(f)
    newtitle = f'atest0317 测试es同步 bulk{i}'
    data['title'] = newtitle
    data['jobFunctions'][0]['enumId'] = random.choice(jf)
    data['requiredSkills'][0]['skillName'] = random.choice(skills)
    data['type'] = random.choice(type_)

    #留记录
    ff = open(fr'{date_dir}\\{newtitle}.yaml','w',encoding='utf-8')
    yaml.dump(data,stream=ff)
    return data

def test_create_jobs(param):
    url = 'https://api-staging.hitalentech.com:8443/apnpublic/api/v1/biz/jobs/'
    data = param
    headers = {
        'Authorization': get_token()['Authorization']}
    method = 'post'
    try:
        params = param['requests']['params']
    except:
        params = None
    resp = RequestsUtil().request(method=method, url=url, json=data, params=params, headers=headers,
                                  proxies=proxies)
    pylogger.alogger.info(f'{param["title"]} : {str(resp.json())}')
    if resp.status_code == 401:
        login()
        return 2
    elif resp.status_code == 200:
        return 1



if __name__ == '__main__':
    '''
        
    '''
    i = 1
    while datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'),'%Y-%m-%d  %H:%M:%S') \
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

    #print(os.path.dirname(os.path.abspath(__file__)))

