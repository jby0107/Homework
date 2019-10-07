# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:38:36 2019

@author: jiang
"""
from PIL import Image
import numpy as np
from urllib import request
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from wordcloud import WordCloud

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
Resp=request.Request(url='https://www.dongqiudi.com/data', headers=headers)  
html_data=request.urlopen(Resp).read().decode('utf-8')
Soup=bs(html_data,'html.parser')
AllTeams=Soup.find_all('a',target='_blank')
WebList=[]
for i in AllTeams[1:-7]:
    WebList.append(i['href'])
NameList=[]
PlayTimesList=[]
ScoreList=[]
for Web in WebList:
    Resp=request.Request(url=Web, headers=headers)  
    html_data=request.urlopen(Resp).read().decode('utf-8')
    Soup=bs(html_data,'html.parser')
    Name=Soup.find_all('span','item3')
    PlayTimes=Soup.find_all('span','item4')
    Score=Soup.find_all('span','item5')
    for i in range(1,len(Name)):
        NameList.append(Name[i].find_all(text=True)[0])
        PlayTimesList.append(PlayTimes[i].find_all(text=True)[0])
        ScoreList.append(Score[i].find_all(text=True)[0])

EfficiencyDict={}
for i in range(len(NameList)):
    if PlayTimesList[i]!='~' and ScoreList[i]!='~' and ScoreList[i]!='0':
        if int(PlayTimesList[i])>=5:
            EfficiencyDict[NameList[i]]=round(int(ScoreList[i])/int(PlayTimesList[i]),3)
MaskImage=np.array(Image.open('火神杯.jpg'))
wordcloud=WordCloud(scale=20,font_path="simhei.ttf",mask=MaskImage,background_color="white",max_font_size=80)
wordcloud=wordcloud.fit_words(EfficiencyDict)
plt.figure(figsize=(12,13))
plt.imshow(wordcloud)
wordcloud.to_file('result.jpg')
        
    
        
        
        
        
        
        
    