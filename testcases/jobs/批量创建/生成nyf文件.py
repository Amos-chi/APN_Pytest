# Time : 2023/3/9 17:57
import json
import os

import yaml

from common.yaml_util import read_yamlfile


def 批量生成yaml():
    f = open('paramdamo.yaml','r',encoding='utf-8')
    fdata = yaml.load(stream=f,Loader=yaml.FullLoader)


    for i in range(40):
        data = fdata[0]
        if i < 9:
            new_title = f'atest job0{i+1} payroll 0310'
        else:
            new_title = f'atest job{i+1} payroll 0310'
        data['title'] = new_title
        ff = open(fr'yamlfiles/{new_title}.yaml','w',encoding='utf-8')
        yaml.dump(data,stream=ff)

def readaslist():
    dir = r'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\testcases\jobs\批量创建\yamlfiles'
    files = os.listdir(dir)
    list_ = []
    for f in files:
        data = read_yamlfile(fr'\testcases\jobs\批量创建\yamlfiles\{f}')
        list_.append(data)
    print(list_)
    return list_



if __name__ == '__main__':
    批量生成yaml()