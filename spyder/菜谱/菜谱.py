# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:44:12 2019

@author: jiang
"""

from urllib import request
from bs4 import BeautifulSoup as bs
import jieba
import pandas as pd
import re
import numpy
import matplotlib.pyplot as plt
from wordcloud import WordCloud

DeleteList=['白糖','调和油','生粉','植物油','味精','色拉油','元贞糖','食盐','盐','料酒','酱油','生抽','老抽','蚝油','鸡精','花椒','胡椒粉','食用油','淀粉','油盐','醋']
'''获取每道菜的连接'''
def GetWeb(Page,Url):
    WebList=[]
    for i in range(1,Page):
        URL=Url+'?&page='+str(i)
        Resp=request.urlopen(URL)
        html_data=Resp.read().decode('utf-8')
        Soup=bs(html_data,'html.parser')
        Web=Soup.find_all('a',target='_blank')
        for i in Web[0:len(Web)-20]:
            WebList.append(i['href'])
    return WebList

'''获取每道菜的材料'''
def GetIngre(WebList):
    IngreList=[]
    for i in WebList:
        URL=i
        try:
            Resp=request.urlopen(URL)
            html_data=Resp.read().decode('utf-8')
            Soup=bs(html_data,'html.parser')
            Ingre=Soup.find_all('h4')
            for i in Ingre[1:]:
                IngreList.append(i.find_all(text=True)[0])
        except request.HTTPError:
            continue
    return IngreList

'''清理数据'''
def CleanIngre(Ingre):
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, Ingre)
    CleanedIngre = ''.join(filterdata)
    return CleanedIngre

'''生成词频字典'''
def GetFreq(IngreList):
    Ingre_df=pd.DataFrame({'Ingre':IngreList})
    Ingre_stat=Ingre_df.groupby(Ingre_df['Ingre'])
    Ingre_stat=Ingre_stat['Ingre'].agg([numpy.size])
    Ingre_stat=Ingre_stat.reset_index()
    Ingre_frequence = {x[0]:x[1] for x in Ingre_stat.head(1000).values}
    for i in DeleteList:
        try:
            del(Ingre_frequence[i])
        except KeyError:
            continue
    return Ingre_frequence
'''主程序生成云图'''
def Main(Page,Url):
    WebList=GetWeb(Page,Url)
    IngreList=GetIngre(WebList)
    Ingre=''
    for i in IngreList:
        Ingre+=i
    CleanedIngre=CleanIngre(Ingre)
    IngreList=jieba.lcut(CleanedIngre)
    Ingre_frequence=GetFreq(IngreList)
    wordcloud=WordCloud(scale=20,font_path="simhei.ttf",background_color="white",max_font_size=80)
    wordcloud=wordcloud.fit_words(Ingre_frequence)
    plt.imshow(wordcloud)
    wordcloud.to_file('result.jpg')
    return Ingre_frequence



a=Main(10,'https://www.meishij.net/china-food/caixi/chuancai/')

    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

