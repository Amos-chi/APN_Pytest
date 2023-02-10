# Time : 2023/2/1 14:16
import pytest

from common.get_Authorization import GetAuthorization
from common.yaml_util import clean_yaml


@pytest.fixture(scope='session',autouse=True)
def sco_session():
    #print('{:-^50}'.format('这里运行了session级别夹具'))
    clean_yaml()
    GetAuthorization().get_Authorization()
    yield
    #print('{:-^50}'.format('所有用例测试结束'))

