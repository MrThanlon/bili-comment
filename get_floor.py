# -*- coding: utf-8 -*-
import urllib,urllib2
import json
from sys import argv

def get_floor(av_number) :
    av_url = 'http://api.bilibili.com/x/reply?oid=' + av_number + '&type=1&pn=1'
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
    req = urllib2.Request(av_url,None)
    response_floor = urllib2.urlopen(req,timeout = 20).read().decode('utf-8')
    key1 = response_floor.find('page')
    key2 = response_floor.find('floor',key1)
    if key2 ==-1 : #连个评论都没有
        return '0'
    key3 = response_floor.find(',',key2)
    return response_floor[key2+7 : key3] #手写json解析，呵呵呵，效率还行
    #json_data = json.loads(response_floor)
    #return json_data['data']['page']['count']
    #return json_data['data']['replies']['floor']

#print get_floor(argv[1])
print get_floor('12203888')