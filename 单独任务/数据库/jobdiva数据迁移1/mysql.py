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



def connection_select(sql):
    # 打开数据库连接
    db = MySQLdb.connect("wuhan.hitalent.com", "root", "1*ni5sCFUWgq", "apnv3-migration", port=13306, charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        # 执行SQL语句
        print(f'当前执行: {sql}')
        result_lenth = cursor.execute(sql)
        #print(f'总数: {result_lenth}')

        #获取表头
        columns = [desc[0] for desc in cursor.description]

        # 获取所有记录列表
        results = cursor.fetchall()

        # 关闭数据库连接
        db.close()

        return columns,results

    except Exception as e:
        print(str(e))


def data_format(results):
    key_list = results[0]

    result_list = []

    for result in results[1]:
        dic = {}
        for i in range(len(key_list)):

            if isinstance(result[i],bytes):
                dic[key_list[i]] = ord(result[i])
            elif isinstance(result[i],datetime.datetime):
                dic[key_list[i]] = datetime.datetime.strftime(result[i], '%Y-%m-%dT%H:%M:%SZ')
            else:
                dic[key_list[i]] = result[i]
        result_list.append(dic)

    return result_list

    # f = open('mysql_select_result.json', 'a', encoding='utf-8')
    # f.truncate(0)
    # f.write(json.dumps(result_list, indent=4, ensure_ascii=False))
    #
    # ff = open('mysql_select_result.csv', 'a', encoding='utf-8', newline='')
    # ff.truncate(0)
    # csvwriter = csv.writer(ff)
    # csvwriter.writerow(key_list)
    #
    # for r in result_list:
    #     list_ = []
    #     for k, v in r.items():
    #         list_.append(v)
    #     csvwriter.writerow(list_)


def select_sql(sql):
    result_list = data_format(connection_select(sql))
    if len(result_list) == 1:
        return result_list[0]
    elif len(result_list) > 1:
        return result_list
    else:
        return {}

if __name__ == '__main__':
    #select_sql("SELECT * FROM company WHERE name = 'Huawei 华为 中国2'")
    select_sql("SELECT * FROM company_address WHERE company_id = '6' and type = '99999'")
    select_sql("SELECT * FROM company_address WHERE company_id = '59' and type = '99999'")