#-*- coding:utf-8 -*-
#多线程测试

import requests
import os
import thread
import time
from multiprocessing import Pool

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
p = Pool()
for tn in range(4) :
    #thread.start_new_thread(sin_thread , ('810872' , str(tn) ,))
    p.apply_async(sin_thread, args=('810872' , tn))
'''
thread.start_new_thread(sin_thread,('810872' , '1' ,))
thread.start_new_thread(sin_thread,('810872' , '2' ,))
thread.start_new_thread(sin_thread,('810872' , '3' ,))
thread.start_new_thread(sin_thread,('810872' , '4' ,))
'''
p.close()
p.join()
print 'hello'
time.sleep(300)
print 'done'