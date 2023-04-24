# Time : 2023/4/24 13:25
import csv
import datetime
import json
from bitstring import BitArray
import MySQLdb

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

key_list = ['id', 'logo', 'name', 'biz_name', 'industry', 'website', 'fortune_rank', 'business_revenue',
                'staff_size', 'linkedin_company_profile', 'crunchbase_company_profile',
                'type', 'client_level_type', 'active', 'tenant_id', 'phone', 'email', 'fax', 'profile', 'description',
                's3_link', 'founded', 'organization_name', 'created_by', 'created_date',
                'last_modified_by', 'last_modified_date', 'source_link', 'puser_id', 'pteam_id']

def connection_select(sql):
    # 打开数据库连接
    db = MySQLdb.connect("wuhan.hitalent.com", "root", "1*ni5sCFUWgq", "apnv3-migration", port=13306, charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        # 执行SQL语句
        result_lenth = cursor.execute(sql)
        print(f'总数: {result_lenth}')

        # 获取所有记录列表
        results = cursor.fetchall()

        # 关闭数据库连接
        db.close()

        return results

    except Exception as e:
        print(str(e))


def data_format(results):

    print(results[0])

    result_list = []

    for result in results:
        dic = {}
        for i in range(30):
            dic[key_list[i]] = result[i]

        dic['active'] = ord(dic['active'])
        dic['created_date'] = datetime.datetime.strftime(dic['created_date'], '%Y-%m-%dT%H:%M:%SZ')
        dic['last_modified_date'] = datetime.datetime.strftime(dic['last_modified_date'], '%Y-%m-%dT%H:%M:%SZ')

        result_list.append(dic)

    f = open('mysql_select_result.json', 'a', encoding='utf-8')
    f.truncate(0)
    f.write(json.dumps(result_list, indent=4, ensure_ascii=False))

    ff = open('mysql_select_result.csv', 'a', encoding='utf-8', newline='')
    ff.truncate(0)
    csvwriter = csv.writer(ff)
    csvwriter.writerow(key_list)

    for r in result_list:
        list_ = []
        for k, v in r.items():
            list_.append(v)
        csvwriter.writerow(list_)


def select_sql(sql):
    data_format(connection_select(sql))

if __name__ == '__main__':
    select_sql("SELECT * FROM company LIMIT 3")