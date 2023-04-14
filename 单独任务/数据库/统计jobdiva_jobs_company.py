# Time : 2023/4/7 10:14
import csv
import json

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

'''
用来统计jobdiva 各公司下有多少job 和job状态
'''

f = open('JobsDetail.json', 'r', encoding='utf-8')
jobs = json.load(f)["RECORDS"]
ff = open('CompanyDetail.json', 'r', encoding='utf-8')
companies = json.load(ff)["RECORDS"]

pairs = {}
companyEumn = {}
for company in companies:
    companyEumn[company['_id']] = company['COMPANYNAME']

for job in jobs:
    try:
        if companyEumn[job['COMPANYID']] not in pairs.keys():
            pairs[companyEumn[job['COMPANYID']]] = [[job['JOBTITLE'],job['JOBSTATUS']]]
        else:
            pairs[companyEumn[job['COMPANYID']]].append([job['JOBTITLE'],job['JOBSTATUS']])
    except Exception as e:
        print(str(e))

fff = open('jobs统计结果.csv','w', encoding='utf-8', newline='')
writer = csv.writer(fff)


for company,jobs in pairs.items():
    company_status = {
    "OPEN": 0,
    "CLOSED": 0,
    "FILLED": 0,
    "CANCELLED": 0,
    "ON HOLD": 0,
    "IGNORED": 0,
    "EXPIRED": 0
}
    for j in jobs:
        status = j[1]
        company_status[status] = company_status[status] + 1

    writer.writerow([company, company_status['OPEN'], company_status['CLOSED'], company_status['FILLED'], company_status['CANCELLED'],
                     company_status['ON HOLD'], company_status['IGNORED'], company_status['EXPIRED']])




