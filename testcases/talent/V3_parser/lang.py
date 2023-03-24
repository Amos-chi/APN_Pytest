language_dict = {
    40 : "英文",
    41 : "中文",
    45 : "韩语",
    46 : "日语",
    57 : "印地语",
    50 : "粤语",
    43 : "德语"
}

jobFunction_dict ={
31:"Engineering & Technical-Others",
13:"UX",
14:"UI / UX-Others",
16:"Artificial Intelligence / Machine Learning",
23:"Mobile Development"
}

minimumDegreeLevel_dict = {
    71:"Bachelor",
    70:"Master",
    66:"Docter",
    67:"法学博士",
    68:"医学博士",
    69:"MBA",
    72:"大专",
    73:"高中"
}

def getLanguageZh(type):
    return language_dict.get(type, str(type))

def getJobFunction(type):
    return jobFunction_dict.get(type, str(type))

def getminimumDegreeLevel(type):
    # print(minimumDegreeLevel_dict.get(type, str(type)))
    return minimumDegreeLevel_dict.get(type, str(type))

