#-*- coding:utf-8 -*-
#主程序
from sys import argv
import urllib,urllib2
import time
import thread

import submmit_comment
import get_floor
import login_cookie
#import check_cookie

#读取配置文件
username = ''
password = ''
av_number = ''
floor = ''
comment = ''
get_refresh = '0'
submmit_refresh = '0'
cookie = ''

def str_out(target_str,space_sign) : #读取配置文件用的
    #space_sign = target_str.find(' ')
    space_sign2 = target_str.find(' ',space_sign+1)
    if space_sign2 > 0 :
            return target_str[space_sign+1 : space_sign2]
    else :
        return target_str[space_sign+1 : ]

#读取配置文件，大概后期会改成json格式
conf_path = 'bili.conf'
conf_file = open(conf_path,'r')
conf_lines = conf_file.readlines()
for line in conf_lines :
    sharp_sign=line.find('#')
    if sharp_sign != -1 : #去除注释
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
    elif var_type == 'submmit_refresh' :
        submmit_refresh = str_out(line,space_sign1)
    elif var_type == 'get_refresh' :
        get_refresh = str_out(line,space_sign1)
    elif var_type == 'submmit_refresh' :
        submmit_refresh = str_out(line,space_sign1)
    else :
        cookie = line[space_sign1 : ] #cookie可能有空格
floor_int = int(floor)
#cookie或者user/password必须有一个
if not cookie or (username and password) :
    raise RuntimeError('No cookie or username.')
if not cookie :
    cookie = login_cookie.get_cookie(login_cookie.get_access_key_kaaass(username,password))

#检测conf有效性
if av_number and floor and comment and cookie :
    current_floor = get_floor.get_floor(av_number,0)
    if current_floor == 'e' :
        raise 'Failed to get floors.'
    if floor_int <= int(current_floor) :
        raise RuntimeError('The floor has been taken.')
    #检测cookie可用性，给av11259766发一条评论试试
    if submmit_comment.submmit_comment('11259766','日常打卡',cookie,'2')[0] != 's' : #发送失败
        raise RuntimeError('Cookie may be not available or need to submmit CAPTCHA.')
#开刷
#查询楼层（多线程，未完成）
def floor_init(thread_total) : #thread_total=查询使用的线程数
    floor_result_m = []
    if int(get_floor.get_floor(av_number,0)) > floor_int :
        raise RuntimeError('The floor has been taken.')
    get_sleep_microsecond = float(get_refresh)/1000  #感觉这个可以不用，拖慢了，查楼不用验证码
    
def floor_cycle(av_number_c,floor_set_c) :
    while (floor_set_c - 3) >= get_floor.get_floor(av_number_c,0) : #这一段可以优化，get_floor初始化会占用资源
        time.sleep(get_sleep_microsecond)


#查询楼层（单线程）
floor_result = []#循环提交评论用的，连刷5次会触发验证码好像
if int(get_floor.get_floor(av_number,0)) > floor_int :
    raise RuntimeError('The floor has been taken.')
get_sleep_microsecond = float(get_refresh)/1000
submmit_sleep_microsecond = float(submmit_refresh)/1000
while int(get_floor.get_floor(av_number,0)) < floor_int-3:
    time.sleep(get_sleep_microsecond)
    #if argv[1] == '-v' :
        #print 'refresh'
for times in range(4) : #提交4次
    floor_result.append(submmit_comment.submmit_comment(av_number,comment,cookie,2)[1])
    #print times
    time.sleep(submmit_sleep_microsecond)
#floor_result = [ submmit_comment.submmit_comment(av_number,comment,cookie,2)[1] for ans in range(4) : time.sleep(submmit_sleep_microsecond) ]
'''
while times >=1 :
    floor_result[times] = submmit_comment.submmit_comment(av_number,comment,cookie,2)[1]
    time.sleep(submmit_sleep_microsecond)
    times -= 1
'''
#while times >=1 :
for floor_range in floor_result :
    if floor_range == floor :
        print 'Done.Good luck.'
        raw_input()
        times = 9982
        break
    times -= 1
if times != 9982 :
    print 'I am sorry.'
    raw_input()
'''
else :
    print 'Done.Good luck.'
    raw_input()
'''