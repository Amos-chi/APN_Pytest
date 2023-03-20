# Time : 2023/3/9 17:57
import datetime
import json
import os
import random
import time

import yaml

from common.yaml_util import read_yamlfile


def 批量生成yaml():
    # PAY_ROLL FULL_TIME CONTRACT
    date_ = datetime.datetime.now().strftime('%Y-%m-%d')
    date_dir = 'yamlfiles_time' + '/' + date_
    if not os.path.exists(date_dir):
        os.makedirs(date_dir)

    f = open('paramdamo.yaml','r',encoding='utf-8')
    fdata = yaml.load(stream=f,Loader=yaml.FullLoader)


    for i in range(100):
        data = fdata[0]
        types = ['PAY_ROLL', 'FULL_TIME', 'CONTRACT']
        type = random.choice(types)
        if i < 9:
            new_title = f'atest job0{i+1} {type} 0317'
        else:
            new_title = f'atest job{i+1} {type} 0317'
        data['title'] = new_title
        data['jobType'] = type
        ff = open(fr'{date_dir}/{new_title}.yaml','w',encoding='utf-8')
        yaml.dump(data,stream=ff)

def readaslist(dir_):
    dir = fr'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\testcases\jobs\批量创建\yamlfiles_time\{dir_}'
    files = os.listdir(dir)
    list_ = []
    for f in files:
        data = read_yamlfile(fr'\testcases\jobs\批量创建\yamlfiles_time\{dir_}\{f}')
        list_.append(data)
    return list_



if __name__ == '__main__':
    批量生成yaml()
    #readaslist('2023-03-13')