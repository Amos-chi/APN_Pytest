#@pytest.fixture(scope='session',autouse=True)
import chardet
import codecs
import csv
import re
import time
from contextlib import ExitStack

import pytest

@pytest.fixture(scope='package',autouse=True)
def bget_encoding():
    print('2222')
    file = 'csvdata/company/company_list.csv'
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        enc = chardet.detect(f.read())['encoding']
        if enc != 'utf-8':
            convert(file, in_code=enc, out_code="UTF-8")
            print('字符集已验证')
        else:
            print('字符集已验证')
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

@pytest.fixture(scope='package',autouse=True)
#def cFromCsvToJson(csv_path):
def cFromCsvToJson(csv_path='csvdata/company/company_list.csv'):
    print('3333')

    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for key in ['feature', 'story', 'title']:
                data = dict(row)
                if not data[key]:
                    data[key] = '"Null"'
            profileList.append(data)
            print('读取csv')
        #print(profileList)
        return profileList

#@pytest.fixture(scope='package',autouse=True)
#def dEnvReplaceYaml11(yaml_file, new_yaml_file):
def dEnvReplaceYaml11(yaml_file, new_yaml_file):

    try:
        with ExitStack() as stack:
            yml_file = stack.enter_context(open(yaml_file, 'r+',encoding='utf-8'))
            yf = open(new_yaml_file, 'w',encoding='utf-8')
            yml_output = stack.enter_context(yf)
            # 先读取YAML模板文件，返回值为字符串列表
            yml_file_lines = yml_file.readlines()
            # profileList的长度即为测试用例的数量
            print('处理csv')
            for i in range(0, len(profileList)):
                # 循环遍历列表
                for line in yml_file_lines:
                    new_line = line
                    # 如果找到以“$csv{”开头的字符串
                    if new_line.find('$csv{') > 0:
                        # 对字符串以“:”切割
                        env_list = new_line.split(':')
                        # 取“:”后面的部分，去掉首尾空格，再以“{”切割，再以“}”切割取出变量名称，比如“name”
                        env_name = env_list[1].strip().split('{', 1)[1].split('}')[0]
                        replacement = ""
                        # 如果name在字典列表的key里
                        if env_name in profileList[i].keys():
                            # 取出name对应的值赋给replacement
                            replacement = profileList[i][env_name]
                            # 用replacement替换掉YAML模板中的“$csv{name}”
                            for j in range(0, len(profileList)):
                                new_line = new_line.replace(env_list[1].strip(), replacement)
                    # 将new_line写入到yml_output文件里
                    yml_output.write(new_line)
                yml_output.write("\n\n")
                yf.flush()
            yf.close()
    except IOError as e:
        print("Error: " + format(str(e)))
        raise

@pytest.fixture(scope='package',autouse=True)
#def dEnvReplaceYaml(yaml_file, new_yaml_file):
def dEnvReplaceYaml(yaml_file='testcases/Companies/target/company_list_target.yml',
                      new_yaml_file='hotdata/company/company_list_new.yaml'):
    print('4444')


    prama_str = re.compile('.*?: (\$csv\{(.*?)\})')

    try:
        with ExitStack() as stack:
            yml_file = stack.enter_context(open(yaml_file, 'r+', encoding='utf-8'))
            yf = open(new_yaml_file, 'w', encoding='utf-8')
            yml_output = stack.enter_context(yf)
            # 先读取YAML模板文件，返回值为字符串列表
            yml_file_lines = yml_file.readlines()
            # profileList的长度即为测试用例的数量
            print('处理csv')
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