# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 23:00:18 2021

@author: picheeng
"""
#批次下載
import requests  #done
import os
from bs4 import BeautifulSoup

import webbrowser

#歌單放這
html="https://www.youtube.com/watch?v=34hd2867q8s&list=PLItPPrnl-gcS907RqG1X_TqsfwcMREzXt"
r = requests.get(html) #將網頁資料GET下來
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
soup2=soup.prettify()
music=[]
current=1
for i in range(1,len(soup2)):
    if i>current:
        #print(soup2.find("videoId",i,len(soup2)))
        
        current=soup2.find("\"videoId\":\"",i,len(soup2))
        #print(current , soup2[current+11:current+22])
        if  soup2[current+11:current+22] not in music and 'html' not in soup2[current+11:current+22] :
            music.append(soup2[current+11:current+22])
        #break
print(music)

for i in music:
    html2="https://www.backupmp3.com/watch?v="+i
    webbrowser.open(html2)  # Go to example.com



#%%
#單次下載

import requests  #done
import os
from bs4 import BeautifulSoup

import webbrowser


html=["",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""]


html=["https://www.youtube.com/watch?v=SYUYu-2TOwM&t=63s"]


for i in html:
    if i=="" : continue
    webbrowser.open(i.split("&")[0].replace("youtube","backupmp3"))  # Go to example.com