# -*- coding: utf-8 -*-
import requests

#thanks to BiliAPI(https://api.kaaass.net author:KAAAsS)
#读取access_key
def get_access_key_reqs(user,passwd) :
    post_data = {'user':user,'passwd':passwd}
    access_key_data = requests.post("https://api.kaaass.net/biliapi/user/login",post_data)
    print access_key_data.status_code
    if access_key_data.status_code == '200' :
        key1 = access_key_res.find('access_key')
        access_key = access_key_res[key1+13 : access_key_res.find('"',key1+14)] #13也一样
        #print access_key
        return access_key
    else :
            raise RuntimeError('Error:' + str(access_key_data.status_code))

#读取cookie
def get_cookie(key) :
    url_cookie = 'https://api.kaaass.net/biliapi/user/sso?access_key=' + key
    cookie_res = requests.get(url_cookie)

print get_access_key_reqs('sakura-wrx@outlook.com','sakura-wrx')