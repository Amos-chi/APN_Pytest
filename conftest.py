# Time : 2023/2/1 14:16

import pytest
import chardet
from common.get_Authorization import GetAuthorization
from common.yaml_util import clean_Auth

# yaml_file为YAML模板文件
# new_yaml_file为新生成的带有测试数据的YAML文件


@pytest.fixture(scope='session', autouse=True)
def asco_session():
    print('{:-^50}'.format('这里运行了session级别夹具'))
    clean_Auth()
    GetAuthorization().get_Authorization()
    yield
    print('{:-^50}'.format('所有用例测试结束'))












































#def orders():
    #sco_session()
    #get_encoding()
    #FromCsvToJson(csv_path='csvdata/company_list.csv')
    #EnvReplaceYaml(yaml_file='csvdata/company_list.csv', new_yaml_file='hotdata/new_yaml_files/company_list_nyf.yaml')

