# Time : 2023/4/14 10:25
import json
import os
from pymongo import MongoClient


def jobdiva_connection():
    # SSH连接
    os.popen(r'ssh -i C:\Users\Administrator\Desktop\jobdiva_amos.chi.pem  -L 3303:10.0.0.70:27017 amos.chi@13.251.44.53')

    # MongoDB连接参数
    mongo_host = '127.0.0.1'
    mongo_port = 3303
    mongo_user = 'jobdiva'
    mongo_password = '!pgJ0dI1@3!2#'
    mongo_auth_source = 'perm'

    # 创建MongoDB客户端
    mongo_client = MongoClient(mongo_host, mongo_port)

    # 连接到MongoDB数据库
    db = mongo_client['jobdiva']  # mongo_database
    db.authenticate(mongo_user, mongo_password, source=mongo_auth_source)
    print('jobdiva 连接成功 ->>')

    return db


def jobdiva_search(db,collection,companyName):

    collection = db[collection]  # 表
    print(f'当前处理: {collection} --> {companyName}')
    results = collection.find({'COMPANYNAME': f'{companyName}'})  # collection.find({"migration_status": {$gt:2}, $or: [{"Active": "No"},{"CITY':": "Santa Clara"}]})
    return results

def tojson(results):
    for r in results:
        print(r)

        # 写入json
        f = open('mongoDB_result.json', 'a', encoding='utf-8')
        f.truncate(0)
        f.write(json.dumps(r, indent=4, ensure_ascii=False))



if __name__ == '__main__':
    db = jobdiva_connection()
    results = jobdiva_search(db, 'CompanyDetail','FannieMae')
    #tojson(results)