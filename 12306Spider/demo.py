#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import base64
import json
from PIL import Image
import user


#url
page_url = 'https://kyfw.12306.cn/otn/resources/login.html'
check_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
code_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64'
login_url = 'https://kyfw.12306.cn/passport/web/login'

headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'kyfw.12306.cn',
        'Origin': 'https://kyfw.12306.cn',
        'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
# 访问登录页面，获取cookie
session = requests.session()
response = session.get(page_url, headers=headers)
# print(response.cookies)

# 下载验证码
img_params = {
        'login_site': 'E',
        'module': 'login',
        'rand': 'sjrand',
        '1560318941389': '',
        'callback': 'jQuery19105025383387084035_1560318413894',
        '_': '1560318413900',
}

code_response = session.get(code_url, params=img_params, headers=headers).text
image_bs64 = re.findall('"image":"(.*?)",', code_response)[0]
image = base64.b64decode(image_bs64)
with open('code.jpg', 'wb') as f:
    f.write(image)
img = Image.open('code.jpg')
img.show()

coord_data = {
    "1":"40,40",
    "2":"120,40",
    "3":"180,40",
    "4":"250,40",
    "5":"40,100",
    "6":"120,100",
    "7":"180,100",
    "8":"250,100",
}
#=====================================================================
# 根据打开的图片识别验证码后手动输入，输入正确验证码对应的位置，例如：2,5
# ---------------------------------------
#         |         |         |
#    1    |    2    |    3    |     4
#         |         |         |
# ---------------------------------------
#         |         |         |
#    5    |    6    |    7    |     8
#         |         |         |
# ---------------------------------------
#======================================================================
answerlist = []
input_answer = input("请输入验证码对应编号：")
answer_list = input_answer.split(' ')
for i in answer_list:
    answerlist.append(coord_data.get(i))
print('answer:'+','.join(answerlist))
answer = ','.join(answerlist)


# 检测验证码
yz_params = {
    "callback": "jQuery19108754385247664451_1555036549517",
    "answer": answer,
    "rand": "sjrand",
    "login_site": "E",
    "_": "1555036549519",
}
check_response = session.get(check_url, params=yz_params, headers=headers).text
# print(check_response)
print(re.findall('"result_message":"(.*?)"',check_response))

# 登录
form_data = {
        'username': user.username,
        'password': user.password,
        'appid': 'otn',
        'answer': answer
}
session.cookies.update({
    'RAIL_EXPIRATION':'1555310364529',
    'RAIL_DEVICEID':'K71MCVMaU_fg6Lr5kLs9K5-HrmV-F-LdSuahWpFSW60X8GmWMZiS06V7InVpguAyYJOmW3cNWKx8Giau-aCZEqehQzwLYRMwjHxr1v1EkKjGTn_iX87fpiWNuGK_jPgg-1PgNgIpFMHeEEfDmXfwdmXX2nGNCcuC',
    'route':'495c805987d0f5c8c84b14f60212447d',
})
login_response = session.post(login_url, data=form_data, headers=headers)
# login_response.encoding = 'utf-8'
# print(re.findall('"result_message":"(.*?)"',login_response.text))
print(login_response.text)
