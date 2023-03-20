# Time : 2023/3/15 9:50
import csv
import datetime
import json
import os
import random
import re

import yaml

from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from common.yaml_util import get_Auth

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

jf = ['386', '6', '387', '20', '408', '43', '16', '410', '405', '406', '407', '402', '401', '403', '404', '409', '14', '12', '13', '191', '190', '264', '17', '223', '165', '265', '18', '166', '149', '32', '182', '80', '388', '392', '393', '394', '395', '391', '180', '397', '396', '400', '28', '399', '390', '398', '389', '218', '197', '194', '193', '196', '195', '203', '201', '200', '202', '215', '211', '212', '213', '214', '209', '208', '207', '206', '198', '216', '204', '217', '35', '4', '163', '266', '233', '155', '156', '159', '236', '232', '235', '237', '161', '267', '245', '244', '241', '248', '240', '243', '242', '246', '247', '239', '171', '257', '258', '170', '256', '169']
industries = ['129', '131', '130', '142', '121', '122', '123', '125', '124', '141', '140', '139', '138', '137', '4', '136', '135', '134', '133', '132', '128', '127', '119', '118']
languages = ['40', '41', '57', '42', '43', '44', '45', '46', '48', '49', '50', '51', '52', '53', '54', '55', '56', '58', '59', '60', '61', '62', '63', '64']
currrency = [0,1,2,3,4]

def 循环生成yaml(n):
    date_ = datetime.datetime.now().strftime('%Y-%m-%d')
    date_dir = f'../testcases/talent/批量创建/yamlfiles_time/循环四小时/{date_}'
    if not os.path.exists(date_dir):
        os.makedirs(date_dir)

    f = open(r'/hotdata/talent/talnet_moduleTest_nyf.yaml', 'r', encoding='utf-8')
    yd = yaml.load(stream=f, Loader=yaml.FullLoader)
    data = yd[0]['requests']['data']
    reg_str = re.compile("'type': 'PHONE', 'contact': '(\d*)'")
    if r1 := reg_str.search(str(data['contacts'])):
        replacenum = int(r1.group(1)) + n-1
        data['contacts'] = [{"type": "PHONE", "contact": f"{replacenum}", "sort": 1},
                   {"type": "EMAIL", "contact": f"{replacenum}@163.com", "sort": 2},
                   {"type": "WECHAT", "contact": f"{replacenum}", "details": None, "sort": 3}]

    lastname_reg_str = re.compile("bulk(\d){0,5}")
    r2 = lastname_reg_str.search(data['lastName'])
    number = int(r2.group(1))
    replace_lastName = f'bulk{number + n-1}'
    data['lastName'] = replace_lastName


    data['jobFunctions'] = [{'enumId': random.choice(jf)}]
    data['industries'] = [{'enumId': random.choice(industries)}]
    data['languages'] = [{'enumId': random.choice(languages)}]
    data['currrency'] = random.choice(currrency)

    ff = open(f'{date_dir}/{data["firstName"]}{data["lastName"]}.json','w',encoding='utf-8')
    ff.write(json.dumps(data,indent=4, ensure_ascii=False))
    return data

def test_create_talents(param):
    url = 'https://api-staging.hitalentech.com:8888/talent/api/v3/talents'
    data = param
    headers = {'Authorization': get_Auth('Authorization')}
    method = 'post'
    try:
        params = param['requests']['params']
    except:
        params = None
    resp = RequestsUtil().request(method=method, url=url, json=data, params=params, headers=headers,
                                  proxies=proxies)
    pylogger.alogger.info(f'{param["lastName"]} : {str(resp.json())}')
    if resp.status_code in [201,412]:
        return 1

if __name__ == '__main__':
    '''
        修改n 修改模板中的联系方式 firstName
        直接运行
    '''
    n = 3
    while datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'),'%Y-%m-%d  %H:%M:%S') \
            < datetime.datetime.strptime("2023-03-17T14:00:00Z", '%Y-%m-%dT%H:%M:%SZ'):
        data = 循环生成yaml(n)
        try:
            num = test_create_talents(data)
            if num == 1:
                n += 1
            else:
                pass
        except Exception as e:
            print(e)

