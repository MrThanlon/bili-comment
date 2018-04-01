#-*- coding:utf-8 -*-
#登出，用于让cookie失效

import requests

def logout(cookie_logout) :
    url_logout_1 = 'https://account.bilibili.com/login?act=exit'
    url_logout_2 = 'https://passport.bilibili.com/login?act=exit'
    header_logout_1 = {
                        'Host': 'account.bilibili.com',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Cookie': cookie_logout
                        }
    header_logout_2 = {
                        'Host': 'passport.bilibili.com',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Cookie': cookie_logout
                        }
    #requests.get(url_logout_1 , headers = header_logout_1)
    res_logout = requests.get(url_logout_2 , header_logout_2).content
    if res_logout.find('成功退出登录！') == -1 :
        raise RuntimeError('failed to logout.')

if __name__ == '__main__' :
    logout('')