# Time : 2023/4/6 15:47
import requests

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
headers = {
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsicmVzX2FwaSJdLCJ1c2VyX25hbWUiOiJ7XCJhY3RpdmF0ZWRcIjp0cnVlLFwiY29tcGFueUlkc1dpdGhBbVwiOlsyMDc0LDIwODEsMjA4NCwyMDg4LDIwODksMjA2NywxMl0sXCJlbWFpbFwiOlwiYW1vcy5jaGlAaW50ZWxsaXByb2dyb3VwLmNvbVwiLFwiZmlyc3ROYW1lXCI6XCJBbW9zXCIsXCJpZFwiOjQxOCxcImlwXCI6XCI5MS4yNDMuODEuOTNcIixcImxhc3ROYW1lXCI6XCJDaGlcIixcInBob25lXCI6XCJcIixcInRlYW1JZFwiOjUyLFwidGVuYW50SWRcIjo0LFwidGltZXpvbmVcIjpcIkFzaWEvU2hhbmdoYWlcIixcInVpZFwiOlwiNDE4LDRcIixcInVzZXJuYW1lXCI6XCJhbW9zLmNoaVwifSIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2ODA3NzMyNDcsImF1dGhvcml0aWVzIjpbIlJPTEVfUFJJTUFSWV9SRUNSVUlURVIiLCJST0xFX0hSIiwiUk9MRV9URU5BTlRfQURNSU4iLCJST0xFX1VTRVIiXSwianRpIjoiYTM1MDU5NGYtMDM0NC00MGJlLTk3NGYtMGM3OGUwYzU4OTc4IiwiY2xpZW50X2lkIjoiYXBpYXBwIn0.llp-eNjhkTPxAw3tbh3Fg_z-UnMcIo9BkSbt81iqI_s"
}
url = 'https://api-staging.hitalentech.com:8888/talent/api/v3/talents/search?page=1&size=600'
data = {"search":
            [{"relation":"AND","condition":[
        {"key":"currentLocation","value":{"data":[{"country":"United States","province":"California"}]}},
        #{"key":"collegeName","value":{"data":["canada"]}},
        {"key":"companyName","value":{"data":["Halifax"],"searchMode":"CURRENT_AND_PAST","relation":"AND"}},
        #{"key":"skills","value":{"data":['java'],"relation":"AND"}}
            ]}],"module":"COMMON_POOL","timezone":"Asia/Shanghai"}

resp = requests.post(url=url,headers=headers,json=data,proxies=proxies)
print(f"{len(resp.json())} 个结果 :")

keywords = ['california', 'Bay Area', 'los angeles', 'santa monica', 'san rafael', 'Fremont', 'foster city', 'san jose', 'mountain view'
            , 'palo alto', 'sunnyvale', 'santa clara', 'ca, usa', 'santa clara', 'cupertino, ca']
for r in resp.json():
    location = r['currentLocation']['originDisplay'].lower()
    n = 0
    for k in keywords:
        if k.lower() in location:
            n = 1
    if n == 0 :
        print(f'{r["fullName"]} --- {location} --- {r["_id"]}')