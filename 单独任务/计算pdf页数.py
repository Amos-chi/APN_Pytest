# Time : 2023/3/22 13:32
import csv
import os

import fitz

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
'''
    用来筛选page大于10的pdf文件
    结果会写到csv里
    直接运行 不需要改参数
'''
f = open('page大于10.csv','w',encoding='utf-8',newline='')
writer = csv.writer(f)
for i in ['cn','en']:
    resumePath = fr'E:\中英文简历总\resume {i}'
    files = os.listdir(resumePath)
    for file in files:
        if file.endswith("pdf"):
            try:
                pdf = fitz.open(resumePath + "\\" + file)
                page = pdf.page_count
                pdf.close()
                if page > 10 :
                    print(f'{file} : {page}')
                    writer.writerow([f'{file}',f'{page}'])
                    f.flush()
            except Exception as e:
                print(e)
