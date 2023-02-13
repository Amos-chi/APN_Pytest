# Time : 2023/2/1 14:16
import codecs
import csv
import time
from contextlib import ExitStack



import pytest
import chardet
from common.get_Authorization import GetAuthorization
from common.yaml_util import clean_yaml

# yaml_file为YAML模板文件
# new_yaml_file为新生成的带有测试数据的YAML文件

@pytest.fixture(scope='session',autouse=True)
def asco_session():
    print('{:-^50}'.format('这里运行了session级别夹具'))
    clean_yaml()
    GetAuthorization().get_Authorization()
    yield
    print('{:-^50}'.format('所有用例测试结束'))

#@pytest.fixture(scope='session',autouse=True)
def bget_encoding():
    file = 'csvdata/company_moddle.csv'
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

#@pytest.fixture(scope='session',autouse=True)
def cFromCsvToJson(csv_path):
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for key in ['feature', 'story', 'title']:
                data = dict(row)
                if not data[key]:
                    data[key] = '"Null"'
            profileList.append(data)
            #print('读取csv')
        #print(profileList)
        return profileList

#@pytest.fixture(scope='session',autouse=True)
def dEnvReplaceYaml(yaml_file, new_yaml_file):
    try:
        with ExitStack() as stack:
            yml_file = stack.enter_context(open(yaml_file, 'r+',encoding='utf-8'))
            yf = open(new_yaml_file, 'w',encoding='utf-8')
            yml_output = stack.enter_context(yf)
            # 先读取YAML模板文件，返回值为字符串列表
            yml_file_lines = yml_file.readlines()
            # profileList的长度即为测试用例的数量
            #print('处理csv')
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


#def orders():
    #sco_session()
    #get_encoding()
    #FromCsvToJson(csv_path='csvdata/company_moddle.csv')
    #EnvReplaceYaml(yaml_file='csvdata/company_moddle.csv', new_yaml_file='hotdata/new_yaml_files/nyf.yaml')

