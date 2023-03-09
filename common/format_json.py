# Time : 2023/3/8 10:11
import json

import yaml

input_ = {"search":[{"relation":"AND","condition":[]}],"module":"JOB","timezone":"Asia/Shanghai","filter":[{"relation":"AND","condition":[{"key":"jobType","value":{"data":["FULL_TIME","CONTRACT"],"relation":"OR"}}]}]}
data = json.dumps(input_,indent=4,ensure_ascii=False)
#print(data)

yf = open(r'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\testcases\jobs\format\job_list.yml','r', encoding='utf-8')
data1 = yaml.load(stream=yf,Loader= yaml.FullLoader)
print(json.dumps(data1,indent=4,ensure_ascii=False))
