#-*- coding:utf-8 -*-
#软件多线程速度测试
#使用thread模块，使用锁来等待子线程退出
#相当低级的方式，建议用threading或者multiprocess
import thread
import time

import get_floor

#查询楼层（多线程，尚未完成，不要使用）
global fin_flag
fin_flag = 0 #结束信号，不会用python signal
global total_query
total_query = 0
def floor_st(av_number , floor , thread_number , lock) :
    global fin_flag
    global total_query
    while True : 
        if fin_flag == 1 :
            lock.release()
            thread.exit()
        current_floor = get_floor.get_floor(av_number , 0)#这一段可以优化，get_floor初始化会占用资源
        #print current_floor + ':' + str(thread_number)
        total_query += 1
        if (floor - 4) >= current_floor :
            fin_flag = 1 
            lock.release()
            thread.exit()

def floor_cycle(av_number , floor , thread_total) : #thread_total=使用的线程数，5左右即可
    locks = [] #存储锁，数量=线程数
    global fin_flag
    global total_query
    for tn in range(thread_total) :
        lock = thread.allocate_lock() #acquire上锁，release解锁
        lock.acquire()
        locks.append(lock)
        thread.start_new_thread(floor_st , (av_number , floor , tn , locks[tn] ,))
    #for tn in range(thread_total) :
        #thread.start_new_thread(floor_st , (av_number , floor , tn , locks[tn] ,))
    #time.sleep(300)
    begin_time = time.time()
    while True :
        print total_query
        time.sleep(0.1)
        if total_query >= 500 :
            fin_flag = 1
            break
    total_time = str(time.time()-begin_time)
    #time.sleep(1)
    print 'total time is ' + total_time
    begin_time = time.time()
    for tn in range(thread_total) :
        while locks[tn].locked() :
            fin_flag = 1
    print 'wait for thread using ' + str(time.time() - begin_time)
    print 'done'

if __name__ == '__main__' :
    floor_cycle('810872' , 105944 , 130)