# -*- coding: utf-8 -*-
#无论pn多大都会有返回，超过总数后总是返回第一页，破站药丸
import requests
import urllib,urllib2
'''
pn =1
url = 'http://api.bilibili.com/x/reply?oid=810872&type=1&pn=' + str(pn)
#json_str = requests.get(url).text.decode('utf-8')
json_str = urllib2.urlopen(url).read().decode('utf-8')
print json_str
'''

pn =1
while True :
    url = 'http://api.bilibili.com/x/reply?oid=810872&type=1&pn=' + str(pn)
    json_res = requests.get(url)
    if json_res.status_code == 404 :
        break
    json_str = json_res.content
    json_file = open("C:\\Users\\hzy\\Desktop\\1\\" + str(pn) + '.json','wb')
    json_file.write(json_str)
    json_file.close
    print pn
    pn += 1