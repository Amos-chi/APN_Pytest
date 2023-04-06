# Time : 2023/4/4 13:56
import json

import requests

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def get_eamils():
    f = open('aaa.csv','r',encoding='utf-8')
    emails = f.read()
    emails = emails.split('\n')
    return emails

def find_talent(ff,email_):


    url = 'https://apiv3.hitalentech.com/talent/api/v3/talents/search?page=1&size=600'
    authorization = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsicmVzX2FwaSJdLCJ1c2VyX25hbWUiOiJ7XCJhY3RpdmF0ZWRcIjp0cnVlLFwiY29tcGFueUlkc1dpdGhBbVwiOltdLFwiZW1haWxcIjpcImFtb3MuY2hpQGludGVsbGlwcm9ncm91cC5jb21cIixcImZpcnN0TmFtZVwiOlwiQW1vc1wiLFwiaWRcIjo0MTgsXCJpcFwiOlwiMjcuMTkuODYuMTEzXCIsXCJsYXN0TmFtZVwiOlwiQ2hpXCIsXCJwaG9uZVwiOlwiXCIsXCJ0ZWFtSWRcIjoxNyxcInRlbmFudElkXCI6NCxcInRpbWV6b25lXCI6XCJBc2lhL1NoYW5naGFpXCIsXCJ1aWRcIjpcIjQxOCw0XCIsXCJ1c2VybmFtZVwiOlwiYW1vcy5jaGlcIn0iLCJzY29wZSI6WyJyZWFkIiwid3JpdGUiXSwiZXhwIjoxNjgwNTk0MDUyLCJhdXRob3JpdGllcyI6WyJUZWFtIExlYWRlcl8xMjA2Il0sImp0aSI6IjZjYzIxMWI3LWMzMGEtNDBkNS04MjhiLWVkOTRlZWJkY2IwYSIsImNsaWVudF9pZCI6ImFwaWFwcCJ9.IqL-SM29_X3xtclhCwpM_H5IIyCLNHUtj37sMkNbQzg'
    header = {
        'authorization' : authorization
    }
    data = {"search":[{"relation":"AND","condition":[{"key":"emails","value":{"data":[email_],"relation":"OR"}}]}],"module":"CANDIDATE","timezone":"Asia/Shanghai"}
    while True:
        try:
            resp = requests.post(url=url, headers=header, json=data, proxies=proxies)

            if resp.json() != []:
                data = resp.json()[0]
                if data['currentLocation']:
                    print(f'{email_} : {resp.status_code} : {resp.json()}')
                    ff.write(f'{email_} : {data["_id"]}\n')
                    ff.flush()
            break
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    ff = open('result.txt', 'w', encoding='utf-8')
    emails = get_eamils()
    for email_ in emails:
        find_talent(ff,email_)