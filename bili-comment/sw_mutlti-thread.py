#-*- coding:utf-8 -*-
#软件多线程速度测试
import thread
import time

import get_floor

#查询楼层（多线程，尚未完成，不要使用）
global fin_flag
fin_flag = 0
global total_query
total_query = 0
def floor_st(av_number , floor , thread_number) :
    global fin_flag
    global total_query
    while True : 
        if fin_flag == 1 :
            thread.exit()
        current_floor = get_floor.get_floor(av_number , 0)#这一段可以优化，get_floor初始化会占用资源
        #print current_floor + ':' + str(thread_number)
        total_query += 1
        if (floor - 4) >= current_floor :
            fin_flag = 1 #大概没必要用锁吧
            thread.exit()

def floor_cycle(av_number , floor , thread_total) : #thread_total=使用的线程数，5左右即可
    global total_query
    for tn in range(thread_total) :
        thread.start_new_thread(floor_st , (av_number , floor , tn))
    #time.sleep(300)
    begin_time = time.time()
    while True :
        print total_query
        time.sleep(0.1)
        if total_query >= 1000 :
            fin_flag = 1
            break
    total_time = str(time.time()-begin_time)
    #time.sleep(1)
    print 'total time is ' + total_time
    print 'done'

floor_cycle('810872' , 105344 , 130)