# Time : 2023/3/10 13:37
import json
import os
import random
import re

import requests
import yaml

from common.yaml_util import read_yamlfile
from testcases.B端.批量创建job.enums import jf,type_,skills

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
def get_param_format():
    input_ = {"thirdPartyLink": "", "department": "", "experienceYearRange": {"gte": 0},
     "publicDesc": "<pre style=\"white-space: break-spaces;\">&nbsp;</pre>", "jobFunctions": [{"enumId": 386}],
     "jobPlateFormId": None, "jobPlateFormJobId": None, "minimumDegreeLevel": None,
     "locations": [{"city": "Belcamp", "country": "United States", "location": "", "province": "Maryland"}],
     "requiredSkills": [{"skillName": "java"}], "status": "OPEN", "title": "atest bulk00", "type": "FULL_TIME",
     "sponsorWorkAuths": None, "uuid": None}

    data = json.dumps(input_, indent=4, ensure_ascii=False)
    print(data)

def get_jobfunctions():
    url = 'https://api-staging.hitalentech.com:8443/apnpublic/api/v2/dict/jobFunctions/creation?type=CN'
    headers = {
        'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsicmVzX2FwaSJdLCJ1c2VyX25hbWUiOiJ7XCJhY3RpdmF0ZWRcIjp0cnVlLFwiZW1haWxcIjpcImlwZ0BhbHRvbW5pLmNvbVwiLFwiZmlyc3ROYW1lXCI6XCJJUEdcIixcImlkXCI6NCxcImxhc3ROYW1lXCI6XCJHcm91cFwiLFwidGVuYW50SWRcIjo2NjYwMDA0LFwidWlkXCI6XCI0LDY2NjAwMDRcIixcInVzZXJuYW1lXCI6XCJmZGJhZDk4MGQwZjcxMDc1MzcxYjFkYjBiNWIxOTNjM1wifSIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2Nzg0MzQwMTEsImF1dGhvcml0aWVzIjpbIlJPTEVfQURNSU4iLCJST0xFX1VTRVIiXSwianRpIjoiNGMyZDRkNTYtNDk2MC00MTZkLWIzMmItODFlZTk4ZGNkODA5IiwiY2xpZW50X2lkIjoiYXBucHVibGljYXBwIn0.blvMplfDVRcpnSFSUM7whhQcQfhEUBMr-yeNh0Vs_ac'
    }
    resp = requests.get(url=url, headers=headers, proxies=proxies)
    print(json.dumps(resp.json(),indent=4,ensure_ascii=False))

def handle_jf():
    f = open('enums.py', 'r', encoding='utf-8')
    data = f.readlines()
    list_ = []
    reg_str = re.compile('"(\d*)",')
    for l in data:
        if n := reg_str.search(l):
            list_.append(n.group(1))
    print(list_)
    ff = open('enums.py', 'w', encoding='utf-8')
    ff.write(','.join(list_))

def create_par_files():
    f = open('传参模板.json','r',encoding='utf-8')
    data = json.load(f)
    print(data)
    for i in range(100):
        if i < 9:
            newtitle = f'atest bulk0{i + 1}'
        else:
            newtitle = f'atest bulk{i + 1}'
        data['title'] = newtitle
        data['jobFunctions'][0]['enumId'] = random.choice(jf)
        data['requiredSkills'][0]['skillName'] = random.choice(skills)
        data['type'] = random.choice(type_)
        ff = open(f'yamlfiles\\{newtitle}.yaml','w', encoding='utf-8')
        yaml.dump(data,stream=ff)

def readaslist():
    dir = r'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\testcases\B端\批量创建job\yamlfiles'
    files = os.listdir(dir)
    list_ = []
    for f in files:
        data = read_yamlfile(fr'\testcases\B端\批量创建job\yamlfiles\{f}')
        list_.append(data)
    print(list_)
    return list_


if __name__ == '__main__':
    create_par_files()