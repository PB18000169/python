# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:13:51 2021

@author: Lenovo
"""
import requests
import time
import os

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




