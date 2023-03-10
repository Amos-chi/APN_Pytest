# Time : 2023/3/10 14:34
import csv
import json
import random
import re
import time

import requests

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

jf = ['386', '6', '387', '20', '408', '43', '16', '410', '405', '406', '407', '402', '401', '403', '404', '409', '14', '12', '13', '191', '190', '264', '17', '223', '165', '265', '18', '166', '149', '32', '182', '80', '388', '392', '393', '394', '395', '391', '180', '397', '396', '400', '28', '399', '390', '398', '389', '218', '197', '194', '193', '196', '195', '203', '201', '200', '202', '215', '211', '212', '213', '214', '209', '208', '207', '206', '198', '216', '204', '217', '35', '4', '163', '266', '233', '155', '156', '159', '236', '232', '235', '237', '161', '267', '245', '244', '241', '248', '240', '243', '242', '246', '247', '239', '171', '257', '258', '170', '256', '169']
industries = ['129', '131', '130', '142', '121', '122', '123', '125', '124', '141', '140', '139', '138', '137', '4', '136', '135', '134', '133', '132', '128', '127', '119', '118']
languages = ['40', '41', '57', '42', '43', '44', '45', '46', '48', '49', '50', '51', '52', '53', '54', '55', '56', '58', '59', '60', '61', '62', '63', '64']
currrency = [0,1,2,3,4]

def changeparam():
    with open(r'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\csvdata\talent\talnet_moduleTest.csv','r',encoding='utf-8') as f:
        data = csv.reader(f)
        header = next(data)

        datalist = []
        for l in data:                              # csv.reader() 不算把内容读取到内存, 需要另外遍历读取
            datalist.append(l)

        f.close()

    ff = open(r'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\csvdata\talent\talnet_moduleTest.csv', 'w',
              encoding='utf-8', newline='')
    writer = csv.writer(ff)
    writer.writerow(header)

    n = 1
    for line in datalist:
        reg_str = re.compile("'type': 'PHONE', 'contact': '(\d*)'")
        if r1 := reg_str.search(line[7]):
            replacenum = int(r1.group(1)) + n
            line[7] = [{"type":"PHONE","contact":f"{replacenum}","sort":1},{"type":"EMAIL","contact":f"{replacenum}@163.com","sort":2},{"type":"WECHAT","contact":f"{replacenum}","details":None,"sort":3}]
            n += 1

        replace_currency = random.choice(currrency)
        line[9] = replace_currency

        replace_industry = random.choice(industries)
        line[11] = [{"enumId": f"{replace_industry}"}]

        replace_jf = random.choice(jf)
        line[12] = [{"enumId": f"{replace_jf}"}]

        replace_lang = random.choice(languages)
        line[13] = [{"enumId": f"{replace_lang}"}]

        writer.writerow(line)



def getindustry():
    url = 'https://api-staging.hitalentech.com:8888/job/api/v3/dict/languages?type=EN'
    headers = {
        'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsicmVzX2FwaSJdLCJ1c2VyX25hbWUiOiJ7XCJhY3RpdmF0ZWRcIjp0cnVlLFwiY29tcGFueUlkc1dpdGhBbVwiOlsyMDc0LDIwODEsMjA4NCwyMDg4LDIwODksMjA2NywxMl0sXCJlbWFpbFwiOlwiYW1vcy5jaGlAaW50ZWxsaXByb2dyb3VwLmNvbVwiLFwiZmlyc3ROYW1lXCI6XCJBbW9zXCIsXCJpZFwiOjQxOCxcImlwXCI6XCI2MS4yMjQuNjguMTA2XCIsXCJsYXN0TmFtZVwiOlwiQ2hpXCIsXCJwaG9uZVwiOlwiXCIsXCJ0ZWFtSWRcIjo1MixcInRlbmFudElkXCI6NCxcInRpbWV6b25lXCI6XCJBc2lhL1NoYW5naGFpXCIsXCJ1aWRcIjpcIjQxOCw0XCIsXCJ1c2VybmFtZVwiOlwiYW1vcy5jaGlcIn0iLCJzY29wZSI6WyJyZWFkIiwid3JpdGUiXSwiZXhwIjoxNjc4NDQxNzA2LCJhdXRob3JpdGllcyI6WyJST0xFX1BSSU1BUllfUkVDUlVJVEVSIiwiUk9MRV9IUiIsIlJPTEVfVEVOQU5UX0FETUlOIiwiUk9MRV9VU0VSIl0sImp0aSI6IjdhMGU5ZjA4LTJiNzYtNDlhYi1iNTE3LWVlNTdjNWZjZjdmZiIsImNsaWVudF9pZCI6ImFwaWFwcCJ9.RSMFXk4fGue8EIkSnMo1vtUZsj0NqPR9LC-8dl7Uxwo'
    }
    resp = requests.get(url, headers= headers, proxies= proxies)
    print(json.dumps(resp.json(),indent=4,ensure_ascii=False))




if __name__ == '__main__':
    changeparam()