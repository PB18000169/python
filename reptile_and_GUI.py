# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import get_jmp
import download
import os

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
