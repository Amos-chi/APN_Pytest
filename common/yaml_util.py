# Time : 2023/2/2 10:00
import os

import yaml


# def get_obj_path():
#     return os.path.dirname(__file__).split('common')[0]         # 获取当前文件的路径
from jsonpath import jsonpath


def read_yamlfile(yamldir):
    basedir = 'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest'
    with open(basedir+yamldir, 'r', encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

def get_Auth(key):
    with open('E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\Authorization.yaml','r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader) # yaml.load 语法 , 写入是yaml.dump
        return value[key]

def set_Auth(data):
    with open('E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\Authorization.yaml','a+',encoding='utf-8') as f:
        yaml.dump(data,stream=f,allow_unicode=True)

def clean_Auth():
    with open('E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\Authorization.yaml','w',encoding='utf-8') as f:
        f.truncate()


if __name__ == '__main__':
    pass