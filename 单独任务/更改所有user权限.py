# Time : 2023/4/6 14:29
import json

import requests

from common.requests_util import RequestsUtil

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
header = {
        'authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsicmVzX2FwaSJdLCJ1c2VyX25hbWUiOiJ7XCJhY3RpdmF0ZWRcIjp0cnVlLFwiY29tcGFueUlkc1dpdGhBbVwiOltdLFwiZW1haWxcIjpcImFtb3MuY2hpQGludGVsbGlwcm9ncm91cC5jb21cIixcImZpcnN0TmFtZVwiOlwiQW1vc1wiLFwiaWRcIjo0MTgsXCJpcFwiOlwiOTEuMjQzLjgxLjkzXCIsXCJsYXN0TmFtZVwiOlwiQ2hpXCIsXCJwaG9uZVwiOlwiXCIsXCJ0ZWFtSWRcIjoxNyxcInRlbmFudElkXCI6NCxcInRpbWV6b25lXCI6XCJBc2lhL1NoYW5naGFpXCIsXCJ1aWRcIjpcIjQxOCw0XCIsXCJ1c2VybmFtZVwiOlwiYW1vcy5jaGlcIn0iLCJzY29wZSI6WyJyZWFkIiwid3JpdGUiXSwiZXhwIjoxNjgwNzcwNjEwLCJhdXRob3JpdGllcyI6WyJUZWFtIExlYWRlcl8xMjA2Il0sImp0aSI6IjBlZDE1ZTg2LTEwMWEtNGJlZC1iZTIzLTgzMTVkNTc3ZDk5MiIsImNsaWVudF9pZCI6ImFwaWFwcCJ9.EiBLWO02F4Rwv5drGtzPEnbdfPV_MB-6SMMmjXpx-lU'
    }
'''
租户14 测试代码
'''

def change_users_datescope(userID):
    url = f'https://apiv3.hitalentech.com/user/api/v3/permissions/users/{userID}/data-permissions'

    data = {"teamIds":[],"modifiable":False,"dataScope":2}
    resp = RequestsUtil().request(method='post',url=url, json=data, headers=header, proxies=proxies)


def get_active_users():
    url = 'https://apiv3.hitalentech.com/user/api/v3/users/all-brief'
    resp = requests.get(url = url, headers = header, proxies=proxies)

    active_list = []
    for r in resp.json():
        if r['activated']:
            active_list.append(r['id'])

    return active_list

if __name__ == '__main__':
    #change_users_datescope(721)
    active_list = get_active_users()
    for userID in active_list:
        change_users_datescope(userID)
