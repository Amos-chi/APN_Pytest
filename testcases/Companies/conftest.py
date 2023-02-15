#@pytest.fixture(scope='session',autouse=True)
import os

import chardet
import codecs
import csv
import re
import time
from contextlib import ExitStack

import pytest


@pytest.fixture(scope='package', autouse=True)
def pre():
    #print('00000')
    dir = r'csvdata/company'
    files = os.listdir(dir)
    for i in files:
        if i.endswith('.csv'):
            #@pytest.fixture(scope='package',autouse=True)
            def bget_encoding():
                #print('2222')
                file = f'csvdata/company/{i}'
                # 二进制方式读取，获取字节数据，检测类型
                with open(file, 'rb') as f:
                    enc = chardet.detect(f.read())['encoding']
                    if enc != 'utf-8':
                        convert(file, in_code=enc, out_code="UTF-8")
                        print(f'{i}: 字符集已验证')
                    else:
                        print(f'{i}: 字符集已验证')
                        pass


            def convert(file, in_code="", out_code="UTF-8"):
                try:
                    with codecs.open(file, 'r', in_code) as f_in:
                        new_content = f_in.read()
                        with codecs.open(file, 'w', out_code) as f_out:
                            f_out.write(new_content)

                except IOError as err:
                    print("I/O error: {0}".format(err))


            profileList = []
            # 从csv中读取用例参数, 以字典的列表形式 存放到 profileList , 一个字典就是一个用例
            #@pytest.fixture(scope='package',autouse=True)
            def cFromCsvToJson(csv_path):
            #def cFromCsvToJson(csv_path=f'csvdata/company/{i}'):
                #print('3333')
                #print('读取csv')
                with open(csv_path, 'r', encoding='utf-8') as csv_file:
                    reader = csv.DictReader(csv_file)
                    for row in reader:
                        for key in ['feature', 'story', 'title']:
                            data = dict(row)
                            if not data[key]:
                                data[key] = '"Null"'
                        profileList.append(data)
                    #print(profileList)
                    return profileList

            # 从 profileList 中 读取参数, 按照yaml模板 写入新的yaml中
            format_dir = r'testcases/Companies/format'
            format_files = os.listdir(format_dir)
            ff = ''
            for f in format_files:
                if f[:-11] == i[:-4]:
                    ff = f
            #@pytest.fixture(scope='package',autouse=True)
            def dEnvReplaceYaml(yaml_file, new_yaml_file):
            #def dEnvReplaceYaml(yaml_file=f'testcases/Companies/format/{ff}',
                                  #new_yaml_file=f'hotdata/company/{ff}.yaml'):
                #print('4444')


                prama_str = re.compile('.*?: (\$csv\{(.*?)\})')

                try:
                    with ExitStack() as stack:
                        yml_file = stack.enter_context(open(yaml_file, 'r+', encoding='utf-8'))
                        yf = open(new_yaml_file, 'w', encoding='utf-8')
                        yml_output = stack.enter_context(yf)
                        # 先读取YAML模板文件，返回值为字符串列表
                        yml_file_lines = yml_file.readlines()
                        # profileList的长度即为测试用例的数量
                        #print('处理csv')
                        # print('处理csv')
                        for i in range(0, len(profileList)):
                            # 循环遍历列表
                            for line in yml_file_lines:
                                new_line = line
                                #如果匹配到 $csv{.*?}
                                if r1 := prama_str.search(new_line):
                                    # 取出变量名称，比如“name”
                                    env_name = r1.group(2)
                                    #print('env_name: ' + env_name)
                                    replacement = ""
                                    # 如果name在字典列表的key里
                                    if env_name in profileList[i].keys():
                                        # 取出name对应的值赋给replacement
                                        replacement = profileList[i][env_name]
                                        # 用replacement替换掉YAML模板中的“$csv{name}”
                                        for j in range(0, len(profileList)):
                                            new_line = new_line.replace(r1.group(1), replacement)
                                # 将new_line写入到yml_output文件里
                                yml_output.write(new_line)
                            yml_output.write("\n\n")
                            yf.flush()
                        yf.close()
                except IOError as e:
                    print("Error: " + format(str(e)))
                    raise

    bget_encoding()
    cFromCsvToJson(csv_path=f'csvdata/company/{i}')
    dEnvReplaceYaml(yaml_file=f'testcases/Companies/format/{ff}',
                    new_yaml_file=f'hotdata/company/{i[:-4]}_nyf.yaml')

