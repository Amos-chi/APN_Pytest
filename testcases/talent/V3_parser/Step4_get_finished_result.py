# Time : 2023/3/24 10:35
import datetime
import json
import os

import requests



#链接数据库
# ssh -i C:\Users\Administrator\Desktop\amos.chi.pem  -L 6389:10.0.0.20:6379 amos.chi@13.251.44.53
from redis import Redis

redis_client = Redis('127.0.0.1', port=int(6389), db=0)
d = os.popen(r'ssh -i C:\Users\Administrator\Desktop\amos.chi.pem  -L 6389:10.0.0.20:6379 amos.chi@13.251.44.53')

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
def get_finished_result(header,uuid):
    url_step4 = f'https://api-staging.hitalentech.com:8888/parser/api/v3/parsers/resume/result/{uuid}'
    resp4 = requests.get(url_step4, headers=header, proxies=proxies)
    data = resp4.json().get('data')
    data = json.loads(data)

    #STEP5: 从数据库获取解析时间
    a = redis_client.hget(f'parser:resume:{uuid}:metadata', "last_update_time")
    last_update_time = datetime.datetime.strptime(a.decode(), '%Y-%m-%dT%H:%M:%S.%fZ')

    b = redis_client.hget(f'parser:resume:{uuid}:metadata', "start_time")
    start_time = datetime.datetime.strptime(b.decode(), '%Y-%m-%dT%H:%M:%S.%fZ')

    parser_cost_time = last_update_time.timestamp() - start_time.timestamp()
    print('redis ok..')

    data['start_time'] = b.decode()
    data['last_update_time'] = a.decode()
    data['parser_cost_time'] = parser_cost_time

    # print(data)
    return data