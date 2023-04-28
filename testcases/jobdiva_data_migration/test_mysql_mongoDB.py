# Time : 2023/4/26 10:04
import csv
import json
import os

import pytest
from bson.json_util import dumps

from testcases.jobdiva_data_migration.conftest import get_companies
from 单独任务.数据库.jobdiva数据迁移1.MongoDB import jobdiva_search, jobdiva_connection
from 单独任务.数据库.jobdiva数据迁移1.mysql import select_sql

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}


NewUpdatedCompanyRecords_keys = ['COMPANYID', 'COMPANYNAME', 'COMPANYTYPE', 'EMAIL', 'FAX', 'PHONE', 'STATE', 'URL']
CompanyDetail_keys = ['ADDRESS1', 'Active', 'CITY', 'COMPANYNAME', 'COUNTRY', 'DATEENTERED', 'DATEUPDATED', 'EMAIL', 'FAX', 'ID', 'INDUSTRY', 'PARENTCOMPANYID', 'PARENTCOMPANYNAME']
company_keys = ['id', 'name', 'type', 'website', 'active', 'name', 'created_date', 'last_modified_date', 'email', 'fax', 'id', 'industry']
company_address_keys = ['address', 'city', 'country']
company_sales_lead_client_contact_keys = ['email', 'phone', 'first_name']

class Test_jobdiva_sql():

    r = get_companies()
    db = r[0]
    companyName = r[1]

    @pytest.mark.parametrize('companyName',companyName)
    def jobdiva_apn(self, companyName):

        CompanyDetail = {}
        CompanyDetail_result = jobdiva_search(self.db, 'CompanyDetail',companyName)
        CompanyDetail_result = json.loads(dumps(CompanyDetail_result))[0]
        for key in CompanyDetail_keys:
            CompanyDetail[key] = CompanyDetail_result[key]
        if CompanyDetail['Active'] == 'Yes':
            CompanyDetail['Active'] = 1
        else:
            CompanyDetail['Active'] = 0


        NewUpdatedCompanyRecords = {}
        NewUpdatedCompanyRecords_result = jobdiva_search(self.db, 'NewUpdatedCompanyRecords', companyName)
        NewUpdatedCompanyRecords_result = json.loads(dumps(NewUpdatedCompanyRecords_result))[0]
        for key in NewUpdatedCompanyRecords_keys:
            NewUpdatedCompanyRecords[key] = NewUpdatedCompanyRecords_result[key]

        company = {}
        company_result = select_sql(f"SELECT * FROM company WHERE name = '{companyName}'")
        companyID = company_result['id']
        for key in company_keys:
                company[key] = company_result[key]


        company_address = {}
        company_address_results = select_sql(f"SELECT * FROM company_address WHERE company_id = '{companyID}' and type = '0'")
        for key in company_address_keys:
                company_address[key] = company_address_results[key]

        # company_sales_lead_client_contact = {}
        # company_sales_lead_client_contact_results = []
        # client_contact_results = select_sql(
        #     f"SELECT * FROM company_sales_lead_connect_client_contact WHERE company_id = '{companyID}'")
        # for client_contact in client_contact_results:
        #     company_sales_lead_client_contact_result = select_sql(
        #         f"SELECT * FROM company_sales_lead_client_contact WHERE id = '{client_contact['client_contact_id']}'")
        #
        #     for key in company_sales_lead_client_contact_keys:
        #         company_sales_lead_client_contact[key] = company_sales_lead_client_contact_result[key]
        #     company_sales_lead_client_contact_results.append(company_sales_lead_client_contact)

        f = open('字段对照.csv', 'r', encoding='utf-8')
        rows = csv.reader(f)
        for row in rows:
            if row[1] == 'NewUpdatedCompanyRecords':
                if row[3] == 'company':
                    print(f'比较: {row[1]}: {row[0]} ->> {row[3]}: {row[2]}')
                    print(f'equal: {NewUpdatedCompanyRecords[row[0]]} ->> {company[row[2]]}')
                    if NewUpdatedCompanyRecords[row[0]] == company[row[2]]:
                        print('相等')
                    else:
                        print('{:->20}'.format('  不相等'))
                if row[3] == 'company_result':
                    print(f'比较: {row[1]}: {row[0]} ->> {row[3]}: {row[2]}')
                    print(f'equal: {NewUpdatedCompanyRecords[row[0]]} ->> {company_result[row[2]]}')
                    if NewUpdatedCompanyRecords[row[0]] == company_result[row[2]]:
                        print('相等')
                    else:
                        print('{:->20}'.format('  不相等'))

            if row[1] == 'CompanyDetail':
                if row[3] == 'company':
                    print(f'比较: {row[1]}: {row[0]} ->> {row[3]}: {row[2]}')
                    print(f'equal: {CompanyDetail[row[0]]} ->> {company[row[2]]}')
                    if CompanyDetail[row[0]] == company[row[2]]:
                        print('相等')
                    else:
                        print('{:->20}'.format('  不相等'))
                if row[3] == 'company_result':
                    print(f'比较: {row[1]}: {row[0]} ->> {row[3]}: {row[2]}')
                    print(f'equal: {company_result[row[0]]} ->> {company_result[row[2]]}')
                    if CompanyDetail[row[0]] == company_result[row[2]]:
                        print('相等')
                    else:
                        print('{:->20}'.format('  不相等'))


if __name__ == '__main__':
    Test_jobdiva_sql().jobdiva_apn('Google')
