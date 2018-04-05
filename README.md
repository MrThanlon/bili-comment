# bili-comment
### 哔哩哔哩（https://www.bilibili.com ），抢楼，抢沙发  
### 感谢@KAAAsS( https://kaaass.net )提供获取cookie的方式，没有他我就无法完成使用用户名和密码登录的功能。  
# 请不要恶意使用。  
主程序是bili-comment.py，配置文件是config.json，可以复制config-example.json的内容，json格式
参数说明：  
<table>
<tr><th>Key</th><th>Value</th></tr>
<tr><th>usage</th><th>0=抢特定楼层，1=抢沙发，整数，默认0</tr></th>
<tr><th>username</th><th>用户名</tr></th>
<tr><th>password</th><th>密码</tr></th>
<tr><th>cookie</th><th>api.bilibili.com的cookie，与主站应该一样，可以没有，<br />u&p/cookie二选一，建议用cookie</tr></th>
<tr><th>sofa_mode</th><th>沙发模式，usage=1可用</tr></th>
<tr><th>up_uid</th><th>要抢谁的沙发(usage=1可用)，字符串</tr></th>
<tr><th>floor_mode</th><th>抢楼模式，usage=0可用</tr></th>
<tr><th>av_number</th><th>视频的av号(usage=0可用)，字符串</tr></th>
<tr><th>floor</th><th>要抢的楼层(usage=0可用)，整数</tr></th>
<tr><th>comment</th><th>评论内容，字符串</tr></th>
<tr><th>get_refresh</th><th>刷新间隔，毫秒，整数，默认0</tr></th>
<tr><th>submmit_refresh</th><th>提交评论间隔，毫秒，整数，默认0</tr></th>
<tr><th>multithread</th><th>多线程相关</tr></th>
<tr><th>floor_enabled</th><th>是否启用查楼多线程，0=禁用，1=启用，整数，默认0</tr></th>
<tr><th>thread</th><th>线程数，多线程启用才可用，太快会被反爬，整数，默认5</tr></th>
</table>
