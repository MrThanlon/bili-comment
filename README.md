# bili-comment
哔哩哔哩（https://www.bilibili.com ），抢楼，抢沙发  
感谢@KAAAsS( https://kaaass.net )提供获取cookie的方式，没有他我就无法完成使用用户名和密码登录的功能  
请不要恶意使用  
主程序是bili-comment.py，配置文件是config.json，可以复制config-example.json  
参数说明：  
usage 0=抢特定楼层，1=抢沙发  
username 用户名  
password 密码  
floor 要抢的楼层(usage=0可用)  
up_uid 要抢的up主的沙发(usage=1可用)  
get_refresh 楼层获取刷新间隔，毫秒  
submmit_refresh 提交评论间隔，建议0  
cookie 登录的cookie，可以没有，u/p二选一，建议用cookie  
