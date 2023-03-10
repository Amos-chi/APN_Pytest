# Time : 2023/3/8 10:11
import csv
import json
import re

import yaml

def aa():
    input_ = [{"id":"-1","label":"Popular Language","labelCn":"Popular Language","children":[{"id":"40","label":"English","labelCn":"英语","value":"40","parentId":"-1","checked":False,"name":"ENGLISH"},{"id":"41","label":"Mandarin","labelCn":"普通话","value":"41","parentId":"-1","checked":False,"name":"MANDARIN"},{"id":"57","label":"Hindi","labelCn":"印地语","value":"57","parentId":"-1","checked":False,"name":"HINDI"},{"id":"42","label":"Spanish","labelCn":"西班牙语","value":"42","parentId":"-1","checked":False,"name":"SPANISH"},{"id":"43","label":"German","labelCn":"德语","value":"43","parentId":"-1","checked":False,"name":"GERMAN"},{"id":"44","label":"French","labelCn":"法语","value":"44","parentId":"-1","checked":False,"name":"FRENCH"},{"id":"45","label":"Korean","labelCn":"韩语","value":"45","parentId":"-1","checked":False,"name":"KOREAN"},{"id":"46","label":"Japanese","labelCn":"日语","value":"46","parentId":"-1","checked":False,"name":"JAPANESE"}],"parentId":"0"},{"id":"-2","label":"Full Language List","labelCn":"Full Language List","children":[{"id":"48","label":"Arabic","labelCn":"阿拉伯语","value":"48","parentId":"-2","checked":False,"name":"ARABIC"},{"id":"49","label":"Burmese","labelCn":"缅甸语","value":"49","parentId":"-2","checked":False,"name":"BURMESE"},{"id":"50","label":"Cantonese","labelCn":"粤语","value":"50","parentId":"-2","checked":False,"name":"CANTONESE"},{"id":"51","label":"Czech","labelCn":"捷克语","value":"51","parentId":"-2","checked":False,"name":"CZECH"},{"id":"52","label":"Danish","labelCn":"丹麦语","value":"52","parentId":"-2","checked":False,"name":"DANISH"},{"id":"53","label":"Dutch","labelCn":"荷兰语","value":"53","parentId":"-2","checked":False,"name":"DUTCH"},{"id":"54","label":"Finnish","labelCn":"芬兰语","value":"54","parentId":"-2","checked":False,"name":"FINNISH"},{"id":"55","label":"Greek","labelCn":"希腊语","value":"55","parentId":"-2","checked":False,"name":"GREEK"},{"id":"56","label":"Hebrew","labelCn":"希伯来语","value":"56","parentId":"-2","checked":False,"name":"HEBREW"},{"id":"58","label":"Italian","labelCn":"意大利语","value":"58","parentId":"-2","checked":False,"name":"ITALIAN"},{"id":"59","label":"Malay","labelCn":"马来语","value":"59","parentId":"-2","checked":False,"name":"MALAY"},{"id":"60","label":"Norsk","labelCn":"挪威语","value":"60","parentId":"-2","checked":False,"name":"NORSK"},{"id":"61","label":"Portuguese","labelCn":"葡萄牙语","value":"61","parentId":"-2","checked":False,"name":"PORTUGUESE"},{"id":"62","label":"Russian","labelCn":"俄语","value":"62","parentId":"-2","checked":False,"name":"RUSSIAN"},{"id":"63","label":"Thai","labelCn":"泰语","value":"63","parentId":"-2","checked":False,"name":"THAI"},{"id":"64","label":"Urdu","labelCn":"乌尔都语","value":"64","parentId":"-2","checked":False,"name":"URDU"}],"parentId":"0"}]

    data = json.dumps(input_,indent=4,ensure_ascii=False)
    print(data)

def bb():
    yf = open(r'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\testcases\jobs\format\job_list.yml','r', encoding='utf-8')
    data1 = yaml.load(stream=yf,Loader= yaml.FullLoader)
    print(json.dumps(data1,indent=4,ensure_ascii=False))


def json_to_yaml():
    f = open(r'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\testcases\jobs\paramdemo\paramdemo.json','r',encoding='utf-8')
    data = f.read()
    jdata = json.loads(data)

    ff = open(r'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\testcases\jobs\paramdemo\paramdamo.yaml','w',encoding='utf-8')
    yaml.dump(jdata,stream=ff,allow_unicode=True) # 写入yaml时要用json格式, 不能dump成字符串格式




if __name__ == '__main__':
    aa()