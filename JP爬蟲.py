import requests  #done
import os
from bs4 import BeautifulSoup
PICALL=1
for i in range(10000,90000):
    print(i)
    html="https://erogazou-choice.com/%e7%9b%97%e6%92%ae%e3%82%a8%e3%83%ad%e7%94%bb%e5%83%8f/"+str(i)+".html"
    r = requests.get(html) #將網頁資料GET下來
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
    #print(soup)
    sel = soup.select("content-waku")
    資料夾=r"C:\Users\picheeng\Desktop\python\日本爬蟲"
    for link2 in soup.find_all('a') :
        link=link2.get('href')
        #print(link.get('href'))
        
        if link is not None:
            if html.split("/")[-1].split(".")[0] in link and link[-3:]=="jpg":
                try:
                    print("save "+link)
                    c=link
                    filepath=資料夾+"\\"+"erogazou-choice.com"+"\\("+str(i)+")"+str(soup.title).split(">")[1].split("<")[0].split("|")[0]+c.split("/", -1)[-1]
                    if os.path.isfile(filepath):
                        filepath=filepath
                        print(filepath,"已存在 , 不執行下載")
                    else:
                        pic=requests.get(c)
                        img2 = pic.content
                        #print(str(filepath)+"已下載 "+str(newpic))
                        #newpic=newpic+1
                        pic_out = open(資料夾+"\\"+"erogazou-choice.com"+"\\("+str(i)+")"+str(soup.title).split(">")[1].split("<")[0].split("|")[0]+c.split("/", -1)[-1] ,'wb')
                        pic_out.write(img2)
                        print ("PICALL",PICALL)
                        PICALL=PICALL+1
                        pic_out.close()
                except:
                    continue

#%% done



import requests
import os
import time
from bs4 import BeautifulSoup
allpic=1
for i in range(10000,99999):
    print(i)
    htmlall=["https://erogazoo555.com/"+str(i)+".html"]
    #html="https://erogazoo555.com/10044.html"
    for html in htmlall:
        try:
            r = requests.get(html) #將網頁資料GET下來
            soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
            #print(soup)
            sel = soup.select("content-waku")
            
            資料夾=r"C:\Users\picheeng\Desktop\python\日本爬蟲"
            for link2 in soup.find_all('a') :
                link=link2.get('href')
                #print(link)
            
                if link is not None:
                    if link[-3:]=="jpg":
                        c=link
                        print("save "+link+" as "+str(soup.title).split(">")[1].split("<")[0]+c.split("/", -1)[-1])
                        filepath=資料夾+"\\"+"erogazoo555"+"\\"+"("+str(i)+")"+str(soup.title).split(">")[1].split("<")[0]+c.split("/", -1)[-1]
                        if os.path.isfile(filepath):
                            filepath=filepath
                            print(filepath,"已存在 , 不執行下載")
                        else:
                            pic=requests.get(c)
                            img2 = pic.content
                            #print(str(filepath)+"已下載 "+str(newpic))
                            #newpic=newpic+1
                            pic_out = open(資料夾+"\\"+"erogazoo555"+"\\"+"("+str(i)+")"+str(soup.title).split(">")[1].split("<")[0]+c.split("/", -1)[-1] ,'wb')
                            pic_out.write(img2)
                            pic_out.close()
                            print(allpic , " pics download")
                            allpic=allpic+1
                            time.sleep(1)
        except:
            continue
        


#%%  已下載完畢
import requests
import os
from bs4 import BeautifulSoup

for ii in range(2,261):
    print(ii)
    htmlall=["http://nudistbeauty.blogy.top/page/"+str(ii)+"/"]
    
    
    #html="https://erogazoo555.com/10044.html"
    for html in htmlall:
        r = requests.get(html) #將網頁資料GET下來
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        #print(soup)
    
        資料夾=r"C:\Users\picheeng\Desktop\python\日本爬蟲"
        for link2 in soup.find_all('a') :
            link=link2.get('href')
            #print(link)
            if link is not None:
                if link[0:7]=='/image/':
                    html="http://nudistbeauty.blogy.top/"+link
                    r = requests.get(html)
                    soup = BeautifulSoup(r.text,"html.parser")
                    #print(soup)
                    for link3 in soup.find_all('img'):
                        #print(link3['src'])
                        if link3['src'][0:7]=='/pictur':
                            #print (link3['src']) 
                            link="http://nudistbeauty.blogy.top/"+link3['src']
                            print("save "+link+" as "+str(soup.title).split(">")[1].split("<")[0]+c.split("/", -1)[-1])
                            c=link
                            pic=requests.get(c)
                            img2 = pic.content
                            #print(str(filepath)+"已下載 "+str(newpic))
                            #newpic=newpic+1
                            pic_out = open(資料夾+"\\"+"beachgirl"+"\\"+str(soup.title).split(">")[1].split("<")[0]+c.split("/", -1)[-1] ,'wb')
                            pic_out.write(img2)
                            pic_out.close()

#%%  C3

import requests
import os
import time
from bs4 import BeautifulSoup
pic2=1
for count in range(52469,80000):
    print("now download " , count)
    htmlall=["http://fightingirl.com/panchira/archive/"+str(count)+"/"]
    #html="http://fightingirl.com/panchira/archive/26466/"
    web="http://fightingirl.com"
    for html in htmlall:
        r = requests.get(html) #將網頁資料GET下來
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        #print(soup)
        #sel = soup.select("content-waku")
        
        資料夾=r"C:\Users\picheeng\Desktop\python\日本爬蟲"
        for link2 in soup.find_all('img'):
            link=link2.get('src')
            #print(link)
            if link is not None and link[:29]=="/panchira/wp-content/uploads/":
                print("save "+link+" , download "+str(pic2)+" pictures")
                pic2=pic2+1
                c=web+link
                filepath=資料夾+"\\"+"fightingirl"+"\\("+str(count)+")"+str(soup.title).split(">")[1].split("<")[0].split("|")[0].replace("?","").replace("/","").replace("*","")+c.split("/", -1)[-1]
                if os.path.isfile(filepath):
                    filepath=filepath
                    print(filepath,"已存在 , 不執行下載")
                else:
                    pic=requests.get(c)
                    img2 = pic.content
                    #print(str(filepath)+"已下載 "+str(newpic))
                    #newpic=newpic+1
                    picpath=資料夾+"\\"+"fightingirl"+"\\("+str(count)+")"+str(soup.title).split(">")[1].split("<")[0].split("|")[0].replace("?","").replace("/","").replace("*","")+c.split("/", -1)[-1]
                    picpath=picpath.split("?")[0]
                    pic_out = open( picpath,'wb')
                    pic_out.write(img2)
                    pic_out.close()
                    time.sleep(1)

#%% console 4
import requests
import os
from bs4 import BeautifulSoup
PICALL=1
request=0
子目錄集合=[
        "街中素人-エロ画像","filmofsex","jd","ol""gal","cosplay","clerk","jk",
        "お姉さん-エロ画像","hitoduma","livechat",
       "痴女変態","fetish","futomomo","ashi","zenra","swimsuit","entertain",
       "ロリ-エロ画像","cheerleader"]
for 子目錄 in 子目錄集合:
    for i in range(1,33):
        print("i=",i)
        print("request=",request)
        request=request+1
        #html="https://megamich.com/%E8%A1%97%E4%B8%AD%E7%B4%A0%E4%BA%BA-%E3%82%A8%E3%83%AD%E7%94%BB%E5%83%8F/page/"+str(i)+"/"
        html="https://megamich.com/"+子目錄+"/page/"+str(i)+"/"
        r = requests.get(html) #將網頁資料GET下來
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        #print(soup)
        #sel = soup.select("content-waku")
        資料夾=r"C:\Users\picheeng\Desktop\python\日本爬蟲"
        for link2 in soup.find_all('a') :
            link=link2.get('href')
            #print(link)
    
            if 'page' in link:
                break
            if link is not None and link[0:4]=='http' and link[-4:]=='html' and 'megamich' in link:
                print(link)
                r2 = requests.get(link)
                print("request=",request)
                request=request+1
                soup2 = BeautifulSoup(r2.text,"html.parser")
                for link3 in soup2.find_all('img') :
                    #print(link3)
                    link4=link3.get('src')
                    #print(link4)
            
                    
                    if  link4 is not None and link4[-3:]=="jpg":
                        print("save "+link4)
                        c=link4
                        
                        
                        #print(str(filepath)+"已下載 "+str(newpic))
                        #newpic=newpic+1
                        number=link.split("/")[-1].split(".")[0]
                        filepath=資料夾+"\\"+"megamich.com"+"\\"+子目錄+"\\("+str(number)+")"+str(soup2.title).split(">")[1].split("<")[0].split("|")[0].replace("?","")+c.split("/", -1)[-1]
                        path=資料夾+"\\"+"megamich.com"+"\\"+子目錄
                        if not os.path.isdir(path):
                            os.mkdir(path)
                        if os.path.isfile(filepath):
                            filepath=filepath
                            print(filepath,"已存在 , 不執行下載")
                        else:
                            try:
                                pic=requests.get("https://megamich.com/"+c)
                                print("request=",request)
                                request=request+1
                                img2 = pic.content
                                pic_out = open(資料夾+"\\"+"megamich.com"+"\\"+子目錄+"\\("+str(number)+")"+str(soup2.title).split(">")[1].split("<")[0].split("|")[0].replace("?","")+c.split("/", -1)[-1] ,'wb')
                                pic_out.write(img2)
                                print ("PICALL",PICALL)
                                PICALL=PICALL+1
                                pic_out.close()
                                time.sleep(1)
                            except:
                                continue
