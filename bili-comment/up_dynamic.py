# -*- coding: utf-8 -*-
#读取up主视频动态，b站对动态的json做了处理，解析可能要时间，目前不做优化，
#去掉所有反斜杠，'"{' -> '{'   ;   '}"' -> '}'
#动态的json如下，
#https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?visitor_uid=0&host_uid=0&offset_dynamic_id=0
#visitor_uid是浏览者uid，可以是0（匿名），可以用户uid（但是似乎要提交cookie），可以没有
#host_uid应该是up主uid，可以是0（而且有视频，但是没有投稿人，里世界？），不可以没有，否则返回code=-1
#offset_dynamic_id不太确定，但应该类似页数，但不是简单的0，1，2，3，4......，而是一长串数字，目前不解析

import requests
import json

#uid_dynamic=up主uid,str
#type=发布类型，int，8=视频，512=追番（好像只有自己的动态可用），16=小视频，2=图片，64=专栏，......
#但是除了视频外的稿件类型我还没开发评论接口，所以其他的返回rid,int，视频返回aid,int，这两个不知道是不是一样的
#如果找不到就会返回0,int
def up_dynamic(uid_dynamic,type_dynamic) :
    url_dynamic = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?visitor_uid=0&host_uid=' + uid_dynamic +'&offset_dynamic_id=0'
    res_data_dynamic = requests.get(url_dynamic).content
    res_json_dynamic = json.loads(res_data_dynamic.replace("\\" , '').replace('"{' , '{').replace('}"' , '}')) #字符替换，大概可以优化
    #遍历json，查找['data']['cards'][0,1,2,3...18遍历,int]['desc']['type']=type
    for number in range(19) :
        if res_json_dynamic['data']['cards'][number]['desc']['type'] == type_dynamic :
            break
    if res_json_dynamic['data']['cards'][number]['desc']['type'] != type_dynamic :
        return 0
    if type_dynamic == 8 :
        return res_json_dynamic['data']['cards'][number]['card']['aid']
    else :
        return res_json_dynamic['data']['cards'][number]['desc']['rid']

#usage
#print up_dynamic('25347081',8)