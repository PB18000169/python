# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:08:03 2021

@author: Lenovo
"""
import requests
from bs4 import BeautifulSoup
import re

#从待爬网页获得图片内容
def get_jmp_strurl_list(str_url):
    #str_url="https://www.ustc.edu.cn"   #待爬网页的URL,这是一个字符串
    URL=requests.get(str_url)   #这是一个URL对象

    #URL.text为URL对象中的html超文本文件内容
    soup=BeautifulSoup(URL.text,'lxml') #转化成Unicode编码格式

    #看看此时的strhtml，可见其文件结构满足html超文本文件的结构
    #print(soup)
    
    data=soup.select('img')
    jmp_strurl_list=[]
    for item in data:
        result=str_url+"/"+item.get('src')
        jmp_strurl_list.append(result)

    #for jmp_strurl in jmp_strurl_list:
        #print(jmp_strurl)
    return jmp_strurl_list



