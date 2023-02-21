# Time : 2023/2/21 10:28
import re

from jsonpath import jsonpath

from common.yaml_util import read_yamlfile

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def get_extract(respjson, json_):
    res_dict = {}
    for ext_key, ext_value in json_['extract'].items():
        #print(f'------------jsonpath(respjson, ext_value) : {jsonpath(respjson, ext_value)}')

        # 如果列表是纯数字, 不能直接用join拼接 要转一下
        result = jsonpath(respjson, ext_value)

        if type(result[0]) is str:
            res_dict[ext_key] = ', '.join(result).lower()


        elif type(result[0]) is int:
            new_list = []
            for o in result:
                new_list.append(str(o))
            res_dict[ext_key] = ', '.join(new_list)

        #bool
        else:
            res_dict[ext_key] = str(result[0])

    return res_dict

def assert_(res_dict,json_):
   regex_str = re.compile('\{\'.*?\': \'?(.*?)\'?\}')
   rules = json_['validate']
   for r in rules:
       for method,ass_dic in r.items():

           # 相等断言
           if method in ['eq', 'equal', 'equals']:
               for assKey, assValue in ass_dic.items():
                   if assValue:
                       print('this is equal assert ::')
                       print(f'"{str(assValue).lower()}" == "{str(res_dict[assKey]).lower()}"')
                       assert str(assValue).lower() == str(res_dict[assKey]).lower()
                   else:
                       pass

           # 包含断言
           elif method in ['ct','contain']:
               for assKey, assValue in ass_dic.items():
                   if assValue :
                       print('this is contain assert ::')
                       # 如果传参不是字符串, 就通过正则 提取想要的字段 拼接成字符串
                       if type(assValue) != str:
                           #print(f'asskey, assValue: {assKey}, {assValue}')
                           re_result = regex_str.findall(str(assValue))
                           print(f're_result: {re_result}  -------------------------')
                           for r in re_result:
                               assValue = r
                               print(f' "{assValue.lower()}" in "{res_dict[assKey]}"')
                               assert assValue.lower() in res_dict[assKey]
                       else:
                           # 把实际的值带入断言规则 打印
                           print(f'"{assValue.lower()}" in "{res_dict[assKey]}"')
                           assert assValue.lower() in res_dict[assKey]
                   else:
                       pass

           # 用于比较条件是一个集合时, 只满足其中一个 就算assert成功
           elif method in ['orgt']:
               for assKey, assValue in ass_dic.items():
                   if assValue:
                       print('this is or_contain assert ::')
                       # 如果传参不是字符串, 就通过正则 提取想要的字段 拼接成字符串
                       if type(assValue) is list:
                           # print(f'asskey, assValue: {assKey}, {assValue}')
                           re_result = regex_str.findall(str(assValue))
                           print(f're_result: {re_result}  -------------------------')
                           is_orgt = 0
                           for r in re_result:
                               assValue = r
                               new_res_list = []
                               for o in res_dict[assKey]:
                                   if type(o) is not str:
                                       res_dict[assKey].append(str(o))
                               print(f' some of {re_result} in "{res_dict[assKey]}"')
                               if assValue.lower() in res_dict[assKey]:
                                  is_orgt = 1
                           assert is_orgt == 1

                   else:
                       pass

           elif method in ['gt', 'great_than', 'bigger_than']:
               pass

           elif method in ['lt', 'less']:
               pass

if __name__ == '__main__':
    json_ = read_yamlfile('\\hotdata\\company\\company_list_nyf.yaml')[0]
    assert_(json_)

