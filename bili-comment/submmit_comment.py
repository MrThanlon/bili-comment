# -*- coding: utf-8 -*-
#核心，提交评论，需要 cookie，av号，暂不支持楼中楼
import urllib,urllib2
import json
from sys import argv
import get_floor

#常见code，0=正常;61001=实名制;未绑定手机号;12015=发送4次以上需要验证码;

#返回两个变量，第一个变量：成功为's'，失败为'f'，注意如果是usage_arg = 0则不做判断一律返回's'
#usage_arg为工作模式，指定返回的第二个变量，
#若成功，0返回响应，1返回rpid，2返回具体楼层，如果是热门视频可能获取不到楼层，因为这个只仅读取第一页20个评论，后期可能更新，主要看你们发不发issues，
#若失败，0返回响应，1返回code，2返回code，成功的code为0，
#若usage_arg为0，无论如何第一个变量都是字符's'
#快刷时建议使用0，需要准确读取建议用2，1的话rpid一般没什么卵用
def submmit_comment(av_number_submmit,comment_message,user_cookie,usage_arg) :
    #csrf就是cookie里的bili_jct
    key5 = user_cookie.find('bili_jct')
    csrf = user_cookie[key5 + 9 : key5 + 41] #32total
    post_data = {'oid': av_number_submmit,
			             'type':'1',
			             'message': comment_message,
			             'plat':'1',
			             'jsonp':'jsonp',
			             'csrf':csrf
			             }
    post_data_urlencode = urllib.urlencode(post_data)

    url_com = 'https://api.bilibili.com/x/v2/reply/add'
    headerdata = {'Host':'api.bilibili.com',
                            'Connection':'keep-alive',
                            #'Content-Length': '89',#需要计算
                            'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'Origin': 'https://www.bilibili.com',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Referer': 'https://www.bilibili.com/video/av'+ av_number_submmit,
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'zh-CN,zh;q=0.9',
                            'Cookie': user_cookie
                            }
    req = urllib2.Request(url_com,post_data_urlencode,headerdata)
    #print req
    res_data = urllib2.urlopen(req).read() #发送完成，0可以返回了
    if usage_arg == 0 :
        return 's',res_data
    #读取rpid
    response_add = json.loads(res_data)
    #核对rpid和rpid_str，感觉不是很需要
    if response_add['code'] != 0 : #正常是0，其他情况看上面，目前没能力处理验证码，抱歉
        return 'e',response_add['code']
    elif usage_arg == 1 :
        return 's',response_add['data']['rpid']
    #读取楼层,使用get_floor_rpid，注意热门视频有可能无法获取
    rpid = response_add['data']['rpid']
    floor = get_floor.get_floor(av_number_submmit,rpid)
    if floor == 'e' :
        return 'e',response_add['code']
    else :
        return 's',floor

#usage
print submmit_comment('11259766','评论测试','sid=iya1ammw; DedeUserID=305660731; DedeUserID__ckMd5=ed25098e9f842b65; SESSDATA=5b179f0a%2C1522260706%2C06440c96; bili_jct=9c50d2fa663a7b8e1a472d5545b15177',2)