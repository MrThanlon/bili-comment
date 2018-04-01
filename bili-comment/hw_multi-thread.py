#-*- coding:utf-8 -*-
#硬件多进程测试

import requests
import os
import thread
import time
import multiprocessing

import get_floor

fin_flag = 0

def sin_thread(av_number_st,thread_number) :
    aac = 0
    while True :
        aac=aac+1
        #print str(aac) + ':' + thread_number
        '''
        floor_st = get_floor.get_floor(av_number_st , 0)
        print floor_st + ':' + thread_number + ' '
        if fin_flag == 1 :
            break
        '''
if __name__ == '__main__' :
    p1 = multiprocessing.Pool(4)
    for tn in range(4) :
        #thread.start_new_thread(sin_thread , ('810872' , str(tn) ,))
        p1.apply_async(sin_thread, args=('810872' , tn ,))

    time.sleep(300)
    p1.close()
    p1.join()
    print 'hello'
    #time.sleep(300)
    print 'done'