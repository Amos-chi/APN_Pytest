# Time : 2023/3/15 9:50
import datetime
import os
import random
import time

import yaml

from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from common.yaml_util import get_Auth

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

def test_getdata(i):

    date_dir = '../testcases/jobs/批量创建/yamlfiles_time' + '/' + '循环四小时'
    if not os.path.exists(date_dir):
        os.makedirs(date_dir)

    f = open('../testcases/jobs/批量创建/paramdamo.yaml','r',encoding='utf-8')
    fdata = yaml.load(stream=f,Loader=yaml.FullLoader)

    time1 = datetime.datetime.now().strftime('%Y-%m-%d  %H.%M.%S')
    data = fdata[0]
    types = ['PAY_ROLL', 'FULL_TIME', 'CONTRACT']
    type = random.choice(types)
    new_title = f'atest 循环四小时{i} {type} {time1}'
    data['title'] = new_title
    data['jobType'] = type

    #留记录
    ff = open(fr'{date_dir}/{new_title}.yaml','w',encoding='utf-8')
    yaml.dump(data,stream=ff)
    pylogger.alogger.info('aaaaa')
    return data

def test_create_jobs(param):
    url = 'https://api-staging.hitalentech.com:8888/job/api/v3/jobs'
    data = param
    headers = {'Authorization': get_Auth('Authorization')}
    method = 'post'
    try:
        params = param['requests']['params']
    except:
        params = None
    resp = RequestsUtil().request(method=method, url=url, json=data, params=params, headers=headers,
                                  proxies=proxies)
    pylogger.alogger.info(resp.json())

if __name__ == '__main__':
    i = 719
    while datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'),'%Y-%m-%d  %H:%M:%S') \
            < datetime.datetime.strptime("2023-03-15T14:40:00Z", '%Y-%m-%dT%H:%M:%SZ'):
        test_create_jobs(test_getdata(i))
        i += 1
    #print(os.path.dirname(os.path.abspath(__file__)))
