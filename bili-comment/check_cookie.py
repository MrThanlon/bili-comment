# -*- coding: utf-8 -*-
#检测cookie可用性，通过关注一个up，它的uid是25347081
import requests

def check_cookie(cookie) :
    header_cookie = {
        'Host': 'account.bilibili.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://passport.bilibili.com/login?gourl=https%3A%2F%2Faccount.bilibili.com%2Faccount%2Fhome',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': cookie
        }
    up_uid = '25347081'
    cookie_res = requests.get('https://passport.bilibili.com/login?gourl=https://account.bilibili.com/account/home',headers = header_cookie)
    tmp = cookie_res.text.decode('utf-8')
    code = cookie_res.status_code
    print 'done'