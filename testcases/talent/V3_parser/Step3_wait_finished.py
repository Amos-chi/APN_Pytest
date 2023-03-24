# Time : 2023/3/24 11:15

from common.logger_util import pylogger
from common.requests_util import RequestsUtil

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

'''
    这个步骤暂时用不到, 接口调result-status会报错 说简历过期重新上传, 不知道什么原因, 但浏览器上是这么调的
    解决办法是 循环调 resume/status 接口, 效果是一样的, 所以这个方法暂时不用
'''
def wait_finished(header, uuid):
    print('进入 wait_finished model')
    url_step3 = f'https://api-staging.hitalentech.com:8888/parser/api/v3/parsers/resume/result-status/{uuid}]'
    while True:
        try:
            #通过uuid查询解析进展 如果没有finished 就一直查
            resp3 = RequestsUtil().request(method='get',url=url_step3, headers = header ,proxies=proxies)
            #print(resp2.content)
            #print(resp2.json())
            if resp3 == 200:
                if resp3.json()['status'] != 'FINISHED':
                    if resp3.json()['status'] == 'EDIT':
                        pylogger().alogger.info('already exist resume!!')
                        break
                    else:
                        pylogger().alogger.info('waiting parser ..   '+ resp3.json()['status'])
                        continue
                else:
                    pylogger().alogger.info('parser success')
                    break
            else:
                pylogger().alogger.info(resp3.json())
                break
        except Exception as e:
            print(str(e))
            continue
