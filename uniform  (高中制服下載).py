import requests
import os
from bs4 import BeautifulSoup
資料夾="uniform高中"
#r = requests.get("http://uniform.wingzero.tw/school/album/tw/"+str(dd)+"/"+str(bb)) #將網頁資料GET下來
#soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
newpic=1
for dd in range(1,560):
    print (dd)
    for bb in range(1,60):
        r = requests.get("http://uniform.wingzero.tw/school/album/tw/"+str(dd)+"/"+str(bb)) #將網頁資料GET下來
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        # print(soup.prettify())
        #print(dd,"-",bb)
   
        sel = soup.select("div.box img") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
        
        
        
# =============================================================================
#         for i in range(0,len(soup.get_text())):
#             if soup.get_text()[i]=="縣" or soup.get_text()[i]=="市" :
#                 location=(soup.get_text()[i-2:i+1])
#                 break
# =============================================================================
        
        p = soup.find_all('span')
        paragraphs = []
        for x in p:
            paragraphs.append(str(x))
        location=paragraphs[3].split(">")[1].split("<")[0]
        
        #print(soup.select("div.span"))
        #print (dd,"-",bb,"-",len(sel))
        if len(sel)>0 :
            a=[]
            for s in sel:
                a.append(s["data-src"])
            #print(a)
            #print(a[0].split("/",-1)[-1])
            temp=str(soup.title)
            school=(temp.split(">",-1)[1].split(" ",-1)[0])
            #print(school)
            for c in a:
                if not os.path.isdir('C:\\Users\\picheeng\\Desktop\\python\\'+資料夾+'\\'+location):
                    os.mkdir('C:\\Users\\picheeng\\Desktop\\python\\'+資料夾+'\\'+location)
                
                path = 'C:\\Users\\picheeng\\Desktop\\python\\'+資料夾+'\\'+location+'\\'+ school 
                filepath = 資料夾+'\\'+location+'\\'+ school +"\\"+c.split("/", -1)[-1]
                if not os.path.isdir(path):
                    os.mkdir(path)
                if os.path.isfile(filepath):
                    filepath=filepath
                else:
                    pic=requests.get(c)
                    img2 = pic.content
                    print(str(filepath)+"已下載 "+str(newpic))
                    newpic=newpic+1
                    pic_out = open(資料夾+'\\'+location+'\\'+ school +"\\"+c.split("/", -1)[-1] ,'wb')
                    pic_out.write(img2)
                    pic_out.close()
        else:
            break
print("done")


