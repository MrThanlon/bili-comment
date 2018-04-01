#-*- coding:utf-8 -*-
#主程序
from sys import argv
import urllib,urllib2
import time
import json
import thread

import submmit_comment
import get_floor
import login_cookie
import up_dynamic
#import check_cookie

#读取配置文件
usage = ''
up_uid =''
username = ''
password = ''
av_number = ''
floor = 0
comment = ''
get_refresh = '0'
submmit_refresh = '0'
cookie = ''

#json版配置文件
try :
    json_file = open('config.json','r')
    json_conf = json.load(json_file)
    usage = json_conf['usage'] #int
    username = json_conf['username'] #str
    password = json_conf['password'] #str
    up_uid = json_conf['up_uid'] #str
    av_number = json_conf['av_number'] #str
    floor = json_conf['floor'] #int
    comment = json_conf['comment'] #str
    get_refresh = json_conf['get_refresh'] #int
    submmit_refresh = json_conf['submmit_refresh'] #int
    cookie = json_conf['cookie'] #str
except KeyError :
    pass

get_sleep_microsecond = float(get_refresh)/1000 #这个可以不用，会拖慢，查楼不弹验证码，仅用于降低cpu使用
submmit_sleep_microsecond = float(submmit_refresh)/1000
#cookie或者user/password必须有一个
if not (cookie or (username and password)) :
    raise RuntimeError('No cookie or username.')
if not cookie :
    cookie = login_cookie.get_cookie(login_cookie.get_access_key_kaaass(username,password))

#检测conf有效性
if comment :
    current_floor = get_floor.get_floor(av_number,0)
    if current_floor == 'e' :
        raise RuntimeError('Failed to get floors.')
    if floor <= int(current_floor) :
        raise RuntimeError('The floor has been taken.')
    #检测cookie可用性，给av11259766发一条评论试试
    if submmit_comment.submmit_comment('11259766','日常打卡',cookie,'2')[0] != 's' : #发送失败
        raise RuntimeError('Cookie may be not available or need to submmit CAPTCHA.')
#开刷
#这段比较丑陋，我以后会改的吧
#抢沙发模式
if usage == 1 : 
    if not up_uid :
        raise RuntimeError('config file error.')
    #不断刷新up主动态，检测aid变化，变化的时候提交评论
    aid = up_dynamic.up_dynamic(up_uid,8)
    while aid == up_dynamic.up_dynamic(up_uid,8) :
        time.sleep(get_sleep_microsecond)
    submmit_status,floor_res = submmit_comment.submmit_comment(av_number,comment,cookie,2)
    if submmit_status == 's' :
        if floor_res == '1' :
            print 'Done.Good luck.'
        else :
            print 'I am sorry.'
    else :
        raise RuntimeError('failed to submmit.')
    raw_input()
    quit

#抢楼模式
#查询楼层（多线程，未测试，不要使用）
global fin_flag
fin_flag = 0
def floor_st(av_number , floor , thread_number) :
    global fin_flag
    while True : 
        if fin_flag == 1 :
            thread.exit()
        current_floor = get_floor.get_floor(av_number , 0)#这一段可以优化，get_floor初始化会占用资源
        #print current_floor + ':' + str(thread_number)
        if (floor - 4) >= current_floor :
            fin_flag = 1 #大概没必要用锁吧
            thread.exit()
        time.sleep(get_sleep_microsecond) #建议0

def floor_cycle(av_number , floor , thread_total) : #thread_total=使用的线程数，推荐130左右，大约每秒200次
    for tn in range(thread_total - 1) :
        thread.start_new_thread(floor_st , (av_number , floor ,))
    while True :
        time.sleep(0.1) #python没有线程优先级，这个需要自行调校
        if fin_flag == 1 :
            break
    #print 'done'

if usage == 0 :
    if not (av_number and floor) :
        raise RuntimeError('config file error.')
    #查询楼层（单线程）
    if int(get_floor.get_floor(av_number , 0)) > floor :
        raise RuntimeError('The floor has been taken.')
    while int(get_floor.get_floor(av_number , 0)) < floor - 4:
        time.sleep(get_sleep_microsecond)
        #if argv[1] == '-v' :
            #print 'refresh'
    floor_result = []#接收评论后的返回
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