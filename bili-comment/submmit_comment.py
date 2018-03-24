# -*- coding: utf-8 -*-
import urllib,urllib2
from sys import argv

#av_number = argv[1]
#comment_message =argv[2]#评论的内容
#user_cookie = argv[3] #登录后的cookie

def submmit_comment(av_number,comment_message,user_cookie) :
    post_data = {'oid': av_number,
			             'type':'1',
			             'message': comment_message,
			             'plat':'1',
			             'jsonp':'jsonp',
			             'csrf':'13338c4f19c24cb911b07c272504d96c'
			             }
    post_data_urlencode = urllib.urlencode(post_data)

    url_com = 'https://api.bilibili.com/x/v2/reply/add'
    headerdata = {'Host':'api.bilibili.com',
                            'Connection':'keep-alive',
                            #'Content-Length': '89',#需要计算
                            'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'Origin': 'https://www.bilibili.com',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Referer': 'https://www.bilibili.com/video/av'+ av_number,
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'zh-CN,zh;q=0.9',
                            'Cookie': user_cookie
                            }
    req = urllib2.Request(url_com,post_data_urlencode,headerdata)
    #print req

    res_data = urllib2.urlopen(req,timeout = 20)
    response_add = res_data.read().decode('utf-8')
    print response_add
    key1 = response_add.find('rpid')
    key2 = response_add.find(',',key1)
    rpid = response_add[key1+6 : key2]
    rpid_str = response_add[key2+13 : response_add.find('"',key2+13)]
    if rpid == rpid_str :
        url_floor = 'http://api.bilibili.com/x/reply?oid=' + av_number + '&type=1&pn=1'
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
        req = urllib2.Request(url_floor,None)
        response_floor = urllib2.urlopen(req,timeout = 20).read().decode('utf-8')
        key3 = response_floor.find(rpid)
        key4 = response_floor.find('floor',key3)
        return response_floor[key4+7 : response_floor.find(',',key4+7)]
    else :
        return 'f'

print submmit_comment('12203888','hello','sid=5kbthf70; DedeUserID=305660731; DedeUserID__ckMd5=ed25098e9f842b65; SESSDATA=5b179f0a%2C1521920621%2C0f56969e; bili_jct=af7acc016a79b1d6a0ac85f265d3c341')