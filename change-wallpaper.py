#!/usr/bin/env python3

import os
import requests
import re
import time

category = input('category : ')
resolution = '1920x1080'
global page
page = 1
regex = re.compile(r'<img src="(.*)1920x1080.jpg')
def getimgurl(page):
    if page == 1:
        url = 'https://wallpaperscraft.com/catalog/'+category+'/date/'+str(resolution)
    else:
        url = 'https://wallpaperscraft.com/catalog/'+category+'/page'+str(page)+'/date/'+str(resolution)
    source_code = requests.get(url).text
    results = regex.findall(source_code)
    return results
def change():
    global page
    while True:
        links = getimgurl(page)
        for i in links:
            myimg = open('./wlp.jpg','wb')
            imgcontent = requests.get('http:'+i+resolution+'.jpg').content
            myimg.write(imgcontent)
            time.sleep(3600)
        page+=1
change()
