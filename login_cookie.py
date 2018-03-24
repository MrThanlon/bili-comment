# -*- coding: utf-8 -*-
import urllib,urllib2

#thanks to BiliAPI(https://api.kaaass.net author:KAAAsS)
def get_access_key(name,passwd) :
    post_data = {
        'user': name ,
        'passwd': passwd
        }
    post_data_urlencode = urllib.urlencode(post_data)
    header_ak = {
        'Host': 'api.kaaass.net',
        #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'User-Agent': 'Firefox',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        #'Content-Length': '47',
        #'Cookie': '__cfduid=dcba472b2a0ce64e301c8f6b3094aecec1521881117; UM_distinctid=162572ef980195-0c201550a9c4b5-17347840-100200-162572ef982610; CNZZDATA1259827171=1357529764-1521878533-%7C1521878533',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
        }
    url_ak = 'https://api.kaaass.net/biliapi/user/login'
    req = urllib2.Request(url_ak,post_data_urlencode,header_ak)
    res_data = urllib2.urlopen(req,timeout = 20)
    response_ak = res_data.read()#.decode('utf-8')
    return response_ak

fi = open('tmp','w')
fi.write(get_access_key('sakura-wrx@outlook.com','sakura-wrx'))
fi.close