# -*- coding: utf-8 -*-
#读取当前楼层，需要 av号
import urllib,urllib2
import requests
import json
import time
from sys import argv

#rpid = 0:读取最高楼层
#rpid != 0:读取所在楼层，如果找不到则返回e
#rpid为int，返回str
def get_floor(av_number_get_floor,rpid) : 
    av_url = 'http://api.bilibili.com/x/reply?oid=' + av_number_get_floor + '&type=1&pn=1'
    #大概不需要
    headerdata = {'Host':'api.bilibili.com',
                            'Connection':'keep-alive',
                            'Cache-Control': 'max-age=0',
                            #'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'zh-CN,zh;q=0.9'#,
                            #'Cookie': user_cookie #可以不需要
                            }
    '''#这一段有玄学问题，改用requests
    req = urllib2.Request(av_url,None)
    get_floor_res = urllib2.urlopen(req,timeout = 20)
    if get_floor_res.code != 200 :
        raise RuntimeError('Errorcode:' + str(get_floor_res.code))
    response_floor = get_floor_res.read()
    '''
    get_floor_res = requests.get(av_url,headers = headerdata)
    if get_floor_res.status_code != 200 :
        raise RuntimeError('Error code:' + str(get_floor_res.code))
    response_floor = get_floor_res.content
    if rpid == 0 :
        key1 = response_floor.find('page')
        key2 = response_floor.find('floor',key1)
        if key2 ==-1 : #连个评论都没有
            return '0'
        key3 = response_floor.find(',',key2)
        return response_floor[key2+7 : key3] #手写json解析，呵呵呵，效率还行
        #json_data = json.loads(response_floor)
        #return json_data['data']['page']['count']
        #return json_data['data']['replies']['floor']
    else :
        key4 = response_floor.find(str(rpid)) #数据太多，用json得到明年了，只爬当前页，20个评论，如果太热门不一定找得到
        if key4 != -1 :
            response_floor.find(str(rpid),key4)
            key5 = response_floor.rfind('floor',0,key4)
            return response_floor[key5 + 7 : response_floor.find(',',key5 + 7)]
        else :
            return 'e'


#print get_floor('11259766',0)