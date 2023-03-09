# Time : 2023/2/21 10:28
import re

from jsonpath import jsonpath

from common.logger_util import pylogger
from common.yaml_util import read_yamlfile

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

# yaml extract部分, 获取resp中的值
def get_extract(respjson, json_):
    res_dict = {}
    if json_.get('extract'):
        for ext_key, ext_value in json_['extract'].items():
            #print(f'------------jsonpath(respjson, ext_value) : {jsonpath(respjson, ext_value)}')

            # 如果列表是纯数字, 不能直接用join拼接 要转一下
            try:
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

            except Exception as e:
                pylogger.alogger.info(f'{e} :: 未从resp中提取到{ext_key}信息')
                pass

        pylogger.alogger.info(f'extract 提取到的字典{res_dict}')
        return res_dict
    else:
        pylogger.alogger.info(f'extract 未配置提取项目')
        return res_dict

def assert_(res_dict,json_):
   # 正则 字典类型的列表 基本都能提取到value 组成一个list 用于ct断言判断  [{"key": "value"},{"key": "value"}]
   regex_str = re.compile('\{\'.*?\': \'?(.*?)\'?\}')

   if json_.get('validate'):
       rules = json_['validate']
       for r in rules:
           for method,ass_dic in r.items():

               # 相等断言
               if method in ['eq', 'equal', 'equals']:
                   for assKey, assValue in ass_dic.items():
                       if assValue:
                           pylogger.alogger.info('--------')
                           try:
                               pylogger.alogger.info(f'this is equal assert ::{assKey}:  "{str(assValue).lower()}" == "{str(res_dict[assKey]).lower()}"')
                               assert str(assValue).lower() == str(res_dict[assKey]).lower()
                           except Exception as e:
                               pylogger.alogger.info(f'yaml.extract 未配置提取项 {assKey}!')
                               raise ValueError
                       else:
                           pass

               # 包含断言
               elif method in ['ct','contain']:
                   for assKey, assValue in ass_dic.items():
                       if assValue :
                           pylogger.alogger.info('--------')
                           # 如果传参不是字符串, 就通过正则 提取想要的字段 拼接成字符串
                           if type(assValue) is list:

                               if type(assValue[0]) is dict:
                                   re_result = regex_str.findall(str(assValue))

                               elif type(assValue[0]) is str:
                                   re_result = assValue

                               for r in re_result:
                                   assValue = r
                                   try:
                                       pylogger.alogger.info(f'this is contain assert ::{assKey}: "{assValue.lower()}" in "{res_dict[assKey]}"')
                                       assert assValue.lower() in res_dict[assKey]
                                   except Exception as e:
                                       pylogger.alogger.info(f'yaml.extract 未配置提取项 {assKey}!')
                                       raise ValueError
                           else:
                               # 把实际的值带入断言规则 打印
                               try:
                                   pylogger.alogger.info(f'this is contain assert ::{assKey}: "{assValue.lower()}" in "{res_dict[assKey]}"')
                                   assert assValue.lower() in res_dict[assKey]
                               except Exception as e:
                                   pylogger.alogger.info(f'yaml.extract 未配置提取项 {assKey}!')
                                   raise ValueError
                       else:
                           pass

               # 用于比较条件是一个集合时, 只满足其中一个 就算assert成功
               elif method in ['orct']:
                   for assKey, assValue in ass_dic.items():
                       if assValue:
                           #pylogger.alogger.info('--or_contain断言--')
                           pylogger.alogger.info('--------')
                           # 如果传参不是字符串, 就通过正则 提取想要的字段 拼接成字符串
                           if type(assValue) is list:
                               re_result = regex_str.findall(str(assValue))
                               try:
                                   pylogger.alogger.info(f'this is or_contain assert ::{assKey}:  some of {re_result} in "{res_dict[assKey]}"')

                                   is_orgt = 0
                                   for r in re_result:
                                       assValue = r

                                       if assValue.lower() in res_dict[assKey]:
                                          is_orgt = 1

                                   assert is_orgt == 1

                               except Exception as e:
                                   pylogger.alogger.info(f'yaml.extract 未配置提取项 {assKey}!')
                                   raise ValueError



                       else:
                           pass

               elif method in ['gt', 'great_than', 'bigger_than']:
                   pass

               elif method in ['lt', 'less']:
                   pass
   else:
       pylogger.alogger.info('no assert rules!')

if __name__ == '__main__':
    json_ = read_yamlfile('\\hotdata\\company\\company_list_nyf.yaml')[0]
    assert_(json_)

