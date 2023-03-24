import datetime
import json
import os
import requests
from requests_toolbelt import MultipartEncoder



from urllib.parse import quote



from common.logger_util import pylogger
from common.requests_util import RequestsUtil
from common.yaml_util import get_Auth
from testcases.talent.V3_parser import getuuid,Step4_get_finished_result
from testcases.talent.V3_parser.Step3_wait_finished import wait_finished

r'''
    RESUME
        parser result to json
        parser result to csv
        ssh -i C:\Users\Administrator\Desktop\amos.chi.pem  -L 6389:10.0.0.20:6379 amos.chi@13.251.44.53
        result json文件已经存在于当日文件夹里的简历 会直接跳过 不会再parser
'''


proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def parserResult(resumePath: str,file: str):

        fileName = os.path.join(resumePath,file)
        uuid = getuuid.get_uuid(fileName)
        urlquote = quote(file)
        pylogger().alogger.info(f'upload and parse {file} ..')

        header = {'Authorization': get_Auth('Authorization')}
        #msword
        #STEP1
        url_step1 = 'https://api-staging.hitalentech.com:8888/parser/api/v3/parsers/resume/status'
        type_enum = {
            '.pdf' : 'pdf',
            '.doc' : 'msword',
            '.docx' : 'vnd.openxmlformats-officedocument.wordprocessingml.document'

        }
        file_type = os.path.splitext(file)[1]
        data_step1 = {
            'uuid': uuid,
            'priority': '0',
            'fileName': urlquote,
            'contentType': f'application/{type_enum[file_type]}'
        }
        while True:
            resp1 = RequestsUtil().request('get',url_step1, params= data_step1, headers = header ,proxies=proxies)
            if resp1.status_code == 200:

                # redis中已有简历存在的情况, 不需要进Step3_wait_finished, 等待parser结束拿结果就行
                if resp1.json()['status'] == 'STARTED':
                    pylogger().alogger.info('waiting parser ..')
                    continue

                elif resp1.json()['status'] == 'NONE':
                    postPolicy = resp1.json()['postPolicy']


                    #STEP2
                    pylogger().alogger.info('STEP1完成, STEP2:开始上传简历 ..')
                    url_step2 = postPolicy['url']
                    name = resp1.json()['fileName']
                    data_step2 = MultipartEncoder({
                        'Content-Type' : f'application/{type_enum[file_type]}',
                        'Content-Disposition': f'filename="{name}"',
                        'x-amz-date': postPolicy['x-amz-date'],
                        'x-amz-signature': postPolicy['x-amz-signature'],
                        'x-amz-algorithm': postPolicy['x-amz-algorithm'],
                        'x-amz-credential': postPolicy['x-amz-credential'],
                        'Policy': postPolicy['policy'],
                        'key': resp1.json()['uuid'],
                        'file': (file, open(os.path.join(resumePath, file), 'rb'), 'application/form-data')
                        })
                    headers = {
                        "Content-Type" : data_step2.content_type
                    }
                    resp2 = RequestsUtil().request('post',url_step2, data= data_step2, proxies=proxies, headers=headers)
                    if resp2.status_code == 204:
                        pylogger().alogger.info('文件上传成功, STEP3: 等待parse ..')

                        continue
                    else:
                        pylogger().alogger.info(resp2.json())
                        break



                elif resp1.json()['status'] == 'FINISHED':
                    pylogger().alogger.info('status: FINISHED')
                    # STEP4: finished后 获取结果
                    data = Step4_get_finished_result.get_finished_result(header, uuid)
                    return data

                elif resp1.json()['status'] == 'EDIT':
                    pylogger().alogger.info(f'err: 该简历已创建候选人. 细节: {json.dumps(resp1.json(),ensure_ascii=False)}')
                    return '该简历已创建候选人'

                else:
                    pylogger().alogger.info(resp1.json())
                    break
            else:
                assert resp1.status_code == 200
                break


if __name__ == '__main__':
    parserResult(r'E:\Parser_Test\resume_files', '高雨然.pdf')