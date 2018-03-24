# -*- coding: utf-8 -*-
import requests
import rsa

#thanks to BiliAPI(https://api.kaaass.net author:KAAAsS)
#读取access_key
def get_access_key_reqs(user,passwd) :
    post_data = {'user':user,'passwd':passwd}
    access_key_data = requests.post("https://api.kaaass.net/biliapi/user/login",post_data)
    print access_key_data.status_code
    if access_key_data.status_code == 200 :
        access_key_text = access_key_res.text.decode('utf-8')
        key1 = access_key_text.find('access_key')
        access_key = access_key_text[key1+13 : access_key_text.find('"',key1+14)] #13也一样
        #print access_key
        return access_key
    else :
            raise RuntimeError('Error:' + str(access_key_data.status_code))

#读取cookie
def get_cookie(key) :
    url_cookie = 'https://api.kaaass.net/biliapi/user/sso?access_key=' + key
    cookie_res = requests.get(url_cookie)
    if cookie_res.status_code == 200 :
        cookie_text = cookie_text.decode('utf-8')
        key1 = cookie_text.find('cookie')  
        return cookie_text[key1+9 : cookie_text.find('"',key1+11)] #+9差不多的，待验证，不确定是9还是10，可能文档有坑
    else :
        raise RuntimeError('Error:failed to get cookie,' + str(cookie_res.status_code))

#自己写的获取access_key的版本
def get_access_key_self(user,passwd) :
    hash_res = requests.get('http://passport.bilibili.com/login?act=getkey')
    tmp = hash_res.status_code
    if hash_res.status_code == 200 :
        hash_text = hash_res.text.decode('utf-8')
        key1 = hash_text.find('hash')
        hash = hash_text[key1+7 : hash_text.find('"',key1+8)].encode('unicode-escape').decode('string_escape') #+7差不多的
        pubkey = rsa.PublicKey.load_pkcs1("-----BEGIN RSA PUBLIC KEY-----\nMIGJAoGBAJ1JwzT2xkmoU9ftu+YHbLqLTwlsexrS/hMdp89sk302hpn0OPPUuZ4u\nRWWZbHUPCAdVb4rstVZPkVXeOiFpxVG5X3zfv5E2e0QrpITzYw9yXt8D752ZbZwu\nUCOwgiStf5oi+9IYK5R9xalYXLdhUOqG4es0ON01xp58khAcxb6xAgMBAAE=\n-----END RSA PUBLIC KEY-----")
        passwd_enc = rsa.encrypt((hash + passwd).encode(),pubkey)
        print passwd_enc
        get_url = 'https://account.bilibili.com/api/login/v2?userid=' + user + '&pwd=' + passwd_enc
        cookie_text = requests.get(get_url).text.decode('utf-8')
        key2 = cookie_text.find('code')
        cookie_code = cookie_text[key2+7 : key2+8] 
        if cookie_code == '0' :
            key3 = cookie_text.find('access_key')
            return cookie_text[key3+14 : cookie_text.find('"',key3+16)] #+14差不多的
        else :
            raise RuntimeError('Error:failed to get cookie.')

    else :
        raise RuntimeError('Error:failed to get public key.')

#def x2

print get_access_key_self('sakura-wrx@outlook.com','sakura-wrx')