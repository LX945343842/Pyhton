登录过程

    登录一般都是POST请求
    
模仿登录过程

1、访问登录页面,获取cookies
    url: https://kyfw.12306.cn/otn/resources/login.html
    method=get
 
2、下载验证码图片
    url:https://kyfw.12306.cn/passport/captcha/captcha-image64
    method=get
    图片以二进制码形式抓取
    
3、检测验证码
    url:https://kyfw.12306.cn/passport/captcha/captcha-check
    method=get
    
    answer: 验证码图片像素坐标参数
    rand: sjrand
    login_site: E
    
4、处理登录请求

    url:https://kyfw.12306.cn/passport/web/login
    method=post  
12306验证码：坐标型验证码
GET请求