# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
import re
import time
import os

#从待爬网页获得图片内容
def get_jmp_strurl_list(strurl):
    str_url="https://www.ustc.edu.cn"   #待爬网页的URL,这是一个字符串
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

def save_img(file_name,jmp_strurl_list):
    #创建保存下载图片的文件夹
    count=0
    mark=1
    unable_jmp_strurl_list=[]
    able_jmp_strurl_list=[]
    if (os.path.exists("./"+file_name)):
        print("the file_name already exists,please change the file_name")
        
    else:
        os.makedirs("./"+file_name)
            
        #开始下载图片
        for jmp_strurl in jmp_strurl_list:
            print(" try downloading----- %s" %(jmp_strurl))
            #通过时延语句判断图片是否可下载
            try:
                jmp_url=requests.get(jmp_strurl,timeout=10)
                time.sleep(1)
            except:
                mark=0;
                
            if(mark==1):
                jmp_full_path="./"+file_name+"/"+str(count)+".jpg"
                with open(jmp_full_path,'wb') as f:
                    f.write(jmp_url.content)
                if not (jmp_strurl in able_jmp_strurl_list):
                    able_jmp_strurl_list.append(jmp_strurl)
                count=count+1
                
            elif(mark==0):
                if not (jmp_strurl in unable_jmp_strurl_list):
                    unable_jmp_strurl_list.append(jmp_strurl)
                    mark=1
                      
        print()
        print("successfully download %d pictures" %(count))
        if(unable_jmp_strurl_list!=[]):
            print("unable download jmp url list:")
            for unable_jmp_strurl in unable_jmp_strurl_list:
                print("   "+unable_jmp_strurl)
   
    return able_jmp_strurl_list


from tkinter import*

def GUI_func():
    strurl=entry1.get()
    file_name=entry2.get()
    jmp_strurl_list=get_jmp_strurl_list(strurl)
    able_jmp_strurl_list=save_img(file_name,jmp_strurl_list)
    
    #显示成功下载的图片信息
    info_window=Tk()
    info_window.title("成功下载----图片的url")
    i=0
    for jmp_strurl in able_jmp_strurl_list:
        Label(info_window,text=jmp_strurl).grid(row=i,column=0)
        i=i+1
    
    #窗口中空一行
    Label(info_window,text="").grid(row=i,column=0)
    i=i+1
    
    #显示图片的路径
    Label(info_window,text="path: "+os.getcwd()).grid(row=i,column=0)
    i=i+1
    pass


myWindow=Tk()
myWindow.title("爬虫----获取网页所有图片")
Label(myWindow,text="input URL").grid(row=0)
Label(myWindow,text="file_name").grid(row=1)

entry1=Entry(myWindow)
entry1.grid(row=0, column=1)
entry2=Entry(myWindow)
entry2.grid(row=1, column=1)

Button(myWindow, text='Quit', command=myWindow.quit).grid(row=2, column=0,sticky=W, padx=5, pady=5)
Button(myWindow, text='Run', command=GUI_func).grid(row=2, column=1, sticky=W, padx=5, pady=5)

myWindow.mainloop()
