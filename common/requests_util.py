# Time : 2023/2/11 15:40

import requests

from common.assert_util import get_extract, assert_
from common.logger_util import pylogger
from common.yaml_util import get_Auth

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
class RequestsUtil():


    def request(self,method,url,**kwargs):
        method = str(method).lower()
        i = 0
        while True:
            try:
                resp = requests.request(method=method,url=url, **kwargs)
                pylogger.alogger.info(f'{method}: {url} - {resp.status_code}')
                break
            except Exception as e :
                print(e)
                i += 1
            finally:
                if i == 5:
                    break

        return resp


    def normal_apis(self,param):
        '''
        常规格式的接口 都可以用这个方法来完成 传参, 请求, 提取extract, 断言
        除了要上传文件的接口 都算常规接口
        :param param: 固件 @pytest.mark.parametrize('param',pre()['xxx']) 中传递的param
        :return:
        '''
        # 显示测试模块 - 用例 - 测试项
        pylogger.alogger.info(f" ---> 测试用例: {param['feature']}. {param['story']}. {param['title']}")
        url = param['requests']['url']
        data = param['requests']['data']
        headers = {'Authorization': get_Auth('Authorization')}
        method = param['requests']['method']
        try:
            params = param['requests']['params']
        except:
            params = None
        resp = RequestsUtil().request(method=method, url=url, json=data, params = params ,headers=headers, proxies=proxies)
        if resp.status_code in [200, 201]:
            if type(resp.json()) is list:
                pylogger.alogger.info(f'{len(resp.json())} results: ')
                n = 1
                for i in resp.json():
                    pylogger.alogger.info(f'第 {n} 个结果: ')
                    res_dict = get_extract(i, param)  # 对每个公司, 获取要断言的字段 , 返回一个字典
                    assert_(res_dict, param)  # 把返回的字典, 和断言规则一起传给assert_方法 进行断言比较
                    n += 1
            if type(resp.json()) is dict:
                res_dict = get_extract(resp.json(), param)
                assert_(res_dict, param)
        else:
            assert resp.status_code == 200



if __name__ == '__main__':
    RequestsUtil().request('qweq','sadasdasd')