# bili-comment
### 哔哩哔哩（https://www.bilibili.com ），抢楼，抢沙发  
### 感谢@KAAAsS( https://kaaass.net )提供获取cookie的方式，没有他我就无法完成使用用户名和密码登录的功能。  
# 请不要恶意使用。  
主程序是bili-comment.py，配置文件是config.json，可以复制config-example.json的内容，json格式
参数说明：  
| key | value |
| :-: | :-: |
| usage | 0=抢特定楼层，1=抢沙发，整数，默认0 |
|username | 用户名 |
|password | 密码 |
| cookie | api.bilibili.com的cookie，与主站应该一样，可以没有，u&p二选一，建议用cookie |
| sofa_mode | 沙发模式，usqge=1可用 |
| up_uid | 要抢谁的沙发(usage=1可用)，字符串 |
| floor_mode | 抢楼模式，usage=0可用 |
| av_number | 视频的av号(usage=0可用)，字符串 |
| floor | 要抢的楼层(usage=0可用)，整数 |
| comment | 评论内容，字符串 |
| get_refresh | 刷新间隔，毫秒，整数，默认0 |
| submmit_refresh | 提交评论间隔，毫秒，整数，默认0 |
| multithread | 多线程相关 |
| 