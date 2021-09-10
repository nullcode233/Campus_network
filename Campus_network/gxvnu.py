#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
#登录地址
post_addr = "http://10.9.9.9/webauth.do?wlanacname=GXVNU-BRAS"
#构造http头部
post_header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'Content-Length':'302',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'JSESSIONID-BOSS-2= ; portalUserCookie= ',
    'Host':'10.9.9.9',
    'Origin':'http://10.9.9.9',
    'Referer':'http://10.9.9.9/webauth.do?wlanacname=GXVNU-BRAS&url=http://www.baidu.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
#构造登录数据
post_data = {
    'loginType':'',
    'auth_type':'0',
    'isBindMac1':'0',
    'pageid':"1",
    'templatetype':"1",
    'listbindmac':"0",
    'recordmac':'0',
    'loginTimes' :"",
    'groupId ':"",
    'distoken':"",
    'echostr':"",
    'url':"http://www.baidu.com",
    'isautoauth': "",
    'notice_pic_float':"/portal/uploads/general/demo1/image/banner.jpg" ,
    'userId':"",#填学号
    'passwd':"",#填密码

    }
#发送post请求登录网页
z = requests.post(post_addr,data=post_data,headers = post_header)
print("登录完成！")