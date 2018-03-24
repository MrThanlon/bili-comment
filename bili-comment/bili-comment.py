#-*- coding:utf-8 -*-
from sys import argv
import urllib,urllib2
import time

#读取配置文件
username = ''
password = ''
av_number = ''
floor = ''
comment = ''
refresh = ''
cookie = ''

def str_out(target_str,space_sign) :
    #space_sign = target_str.find(' ')
    space_sign2 = target_str.find(' ',space_sign+1)
    if space_sign2 > 0 :
            return target_str[space_sign+1 : space_sign2]
    else :
        return target_str[space_sign+1 : ]

def get_floor(number) :
    av_url = 'http://api.bilibili.com/x/reply?oid=' + number + '&type=1&pn=1'
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
    res_data = urllib2.urlopen(req,timeout = 20).read().decode('utf-8')
    key1 = res_data.find('page')
    key2 = res_data.find('floor',key1)
    if key2 ==-1 : #连个评论都没有
        return '0'
    key3 = res_data.find(',',key2)
    return res_data[key2+7 : key3] #手写json解析，呵呵呵，效率还行
    #json_data = json.loads(res_data)
    #return json_data['data']['page']['count']
    #return json_data['data']['replies']['floor']

def submmit_comment(number,comment_message,user_cookie) :
    post_data = {'oid': number,
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
                            'Referer': 'https://www.bilibili.com/video/av'+ number,
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
    if rpid == rpid_str : #查询结果
        url_floor = 'http://api.bilibili.com/x/reply?oid=' + number + '&type=1&pn=1'
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

conf_path = 'bili.conf'
conf_file = open(conf_path,'r')
conf_lines = conf_file.readlines()
for line in conf_lines :
    sharp_sign=line.find('#')
    if sharp_sign>0 : #去除注释
        line = line[0 : sharp_sign]
    space_sign1 = line.find(' ')
    var_type = line[0 : space_sign1]
    if var_type == 'username' :
        username = str_out(line,space_sign1)
    elif var_type == 'password' :
        password = str_out(line,space_sign1)
    elif var_type == 'av_number' :
        av_number = str_out(line,space_sign1)
    elif var_type == 'floor' :
        floor = str_out(line,space_sign1)
    elif var_type == 'comment' :
        comment = line[space_sign1 : ] #comment可能有空格
    elif var_type == 'refresh' :
        refresh = str_out(line,space_sign1)
    else :
        cookie = line[space_sign1 : ] #cookie可能有空格
#读取完成

#查询楼层
floor_int = int(floor)
if int(get_floor(av_number)) > floor_int :
    print 'Mission Failed!'
    input()
    quit()
sleep_microsecond = float(refresh)/1000
while int(get_floor(av_number)) < floor_int-5:
    time.sleep(sleep_microsecond)

#发起评论
while True :
    result_floor = submmit_comment(av_number,comment,cookie)
    if result_floor == floor :
        print 'Mission Completed!'
        input()
        quit()
    elif int(result_floor) > floor_int :
        print 'Mission Failed!'
        input()
        quit()
    elif result_floor == 'f' :
        print 'Config File Error,Try again!'
        input()
        quit()