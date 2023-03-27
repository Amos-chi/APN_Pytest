# Time : 2023/3/23 16:02

import datetime
import json
import os


import fitz

from common.logger_util import pylogger
from testcases.talent.V3_parser import jsonToCsv, uploadAndParse
from testcases.talent.V3_parser.lang import getLanguageZh, getminimumDegreeLevel

r'''
    RESUME
        parser result to json
        parser result to csv
        ssh -i C:\Users\Administrator\Desktop\amos.chi.pem  -L 6389:10.0.0.20:6379 amos.chi@13.251.44.53
        result json文件已经存在于当日文件夹里的简历 会直接跳过 不会再parser
        
        准备好简历 直接运行
'''
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}




def createbyresume(resumePath,file, date_dir):
    exjsons = os.listdir(date_dir)


    # 如果文件正在打开状态 或者 已经有解析过的json文件存在 就跳过
    if file.startswith('~$') :
        pass
    elif f'{file}.json' in exjsons:
        pylogger.alogger.info(f'{file} : 已存在json文件 .')
    else:
        while True:
            try:

                data = uploadAndParse.parserResult(resumePath, file)

                # 将语言栏的数字转换成中文
                languagelist = []
                if data.get('languages'):
                    for l in data['languages']:
                        try:
                            languagelist.append(getLanguageZh(l))
                        except:
                            pass
                data['languages'] = languagelist

                try:
                    if data['educations']:
                        for i in data['educations']:
                            if i['degreeLevel']:
                                i['degreeLevel'] = getminimumDegreeLevel(int(i['degreeLevel']))
                except :
                    pass

                #print(json.dumps(data, indent=4))
                #print(data)

                keys = ['contacts','currentLocation','preferredLocations','languages','educations','experiences','start_time','last_update_time','parser_cost_time']
                newData = {}

                #name
                if data.get('firstName'):
                    newData['firstName'] = data['firstName']
                else:
                    newData['firstName'] = ''

                if data.get('lastName'):
                    newData['lastName'] = data['lastName']
                else:
                    newData['lastName'] = ''

                #keys
                for key in keys:
                    try:
                        newData[key] = data[key]
                    except:
                        newData[key] = ""

                newData['fileName'] = file

                #格式化 education
                if newData['educations'] != '':
                    newedu = []
                    list = ["id", "startDate", "endDate", "collegeName", "degreeLevel", "majorName"]
                    for i in newData['educations']:
                        inew = {}
                        for l in list:
                            if i.get(l) is not None:
                                inew[l] = i[l]
                        newedu.append(inew)
                    newData['educations'] = newedu

                # 格式化 experiences
                if newData['experiences'] != '':
                    newexp = []
                    list = ["id", "description", "companyName", "title", "startDate", "current", "endDate"]
                    for i in newData['experiences']:
                        inew = {}
                        for l in list:
                            if i.get(l) is not None:
                                inew[l] = i[l]
                        newexp.append(inew)
                    newData['experiences'] = newexp

                # 计算页数
                if file.endswith("pdf"):
                    pdf_ = fitz.open(resumePath + "\\" + file)
                    page = pdf_.page_count
                    pdf_.close()
                    newData['page'] = page
                else:
                    newData['page'] = ''

                # size
                size = os.path.getsize(os.path.join(resumePath,file))
                newData['size'] = round(size/1024)

                # fileType
                fileType = os.path.splitext(os.path.join(resumePath,file))[-1][1:]
                newData['fileType'] = fileType

                # skills
                if data.get("skills"):
                #    newData['skills'] = data['skills'] # 平常parser 简历时, 注释这行 释放下面的
                    skilllist = []
                    for f in data['skills']:
                        skilllist.append(f["skillName"])
                    newData['skills'] = ",".join(skilllist)
                else:
                    newData['skills'] = ""

                print('write json ..')
                with open(fr"{date_dir}/{file}.json", "w", encoding='utf-8') as f:
                    f.write(json.dumps(newData, indent=4, ensure_ascii=False))

                print('write csv ..')
                jsonToCsv.json_to_csv(newData)

                break

            except AttributeError:
                pylogger.alogger.info(file + ':' + data + '\n')
                break

            except TypeError as e:
                pylogger.alogger.info(file + ':' + str(e) + '\n')
                print('-------------------------------------error')
                break

            except Exception as e:
                print(e)
                print(file + ':' + str(e))
                continue

if __name__ == '__main__':
    createbyresume(r'E:\Program Files (x86)\PyCharm\Amos-chi\APN_Pytest\testcases\talent\V3_parser\resume_files', '01华为杨先生-金简历-FPGA-11年中南大学本科.pdf')