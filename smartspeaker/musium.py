# -*- coding: utf_8 -*-  
#pytho3.5.1
import csv
import urllib.request
import urllib.parse
import lxml
from bs4 import BeautifulSoup 
import re
import codecs
from time import sleep
 
 #https://www.louvre.fr/jp/oeuvre-notices/%E3%82%B5%E3%83%A2%E3%83%88%E3%83%A9%E3%82%B1%E3%81%AE%E3%83%8B%E3%82%B1
category = {'傑作': 3 ,'フランス革命': 1 ,'ナポレオン-（1769-1821年）': 1 ,'ルイ14世-（1638-1715年）': 2 ,'歴史': 2 ,
            '旅に出る・・・': 2 ,'肖像芸術': 2 ,'風景': 2 ,'装身具': 2 ,'音楽': 2 ,'動物': 2 ,'時間': 2 ,'英雄': 2 ,
             '子ども': 2 ,'聖人': 2 ,'光！': 2 ,'鏡よ鏡！': 1 ,'海辺にて・・・': 2 ,'青': 2 , '王、王妃、皇帝': 4 ,
             '狩猟と漁': 2 , '書く': 2 , '身支度': 2 , '街を守る': 1 , '奇妙な謎': 3 , '美食': 2, '笑顔':2, 
             '祭りで大騒ぎ！': 2, 'ゲームをしましょう！': 2 }    
#category = {'傑作': 3 }
 
 
# -------------------- main --------------------
if __name__ == '__main__':
     
    #for detail_kind in ['mammals']:
        #for number in range(1,162):
            #renumber = '{0:04d}'.format(number)
            #view-source:https://www.louvre.fr/jp/selections/%E5%82%91%E4%BD%9C
            #kesaku = u'%E5%82%91%E4%BD%9C'.encode('ascii', 'ignore').decode('ascii')

    art = []

    for key, value in category.items():
        
        for number in range(0, value):
            url = "https://www.louvre.fr/jp/selections/" + urllib.parse.quote(key) + "?page=" + str(number)
            headers = {
                        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
            }
            print(url)

            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request)
            link = response.read().decode('utf-8')
            soup = BeautifulSoup(link, 'lxml')
            list_pic = soup.findAll("ul",{"class":"list-items-2"})[0]
            
            #print(len(list_pic))

            names = list_pic.findAll("a")

            #詳細ページのURL取得
            for tag in names:
                url = tag.get("href")
                art.append(url)
            

    #Names = ["《オダリスク》"]
    for name in art:
        try:
            #name1 = u'%E3%82%B5%E3%83%A2%E3%83%88%E3%83%A9%E3%82%B1%E3%81%AE%E3%83%8B%E3%82%B1'.encode('ascii', 'ignore').decode('ascii')
            url = "https://www.louvre.fr" + name
            print(url)
            headers = {
                        "User-Agent": "Mozilla/5.0"
            }
            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request).read()
            link = response.decode('utf-8')
            soup = BeautifulSoup(link, 'lxml')

            #タイトル取得
            strong = soup.findAll("div",{"id":"path"})[0]
            title = strong.findAll("strong")[0]

            print(title)

            #説明書き取得
            report = soup.findAll("div",{"class":"col-desc"})[0]
            p = report.findAll("p")[0]

            print(p)

            # fileOpen準備
            csvFile = codecs.open("musiam.csv", "a", "utf-8")

            #csvFileに書き込み準備
            writer = csv.writer(csvFile)
            csvRow = []

            #csvRowにappend
            csvRow.append(name)
            csvRow.append(title)
            csvRow.append(p)
            
            #csvRowを書き出し
            writer.writerow(csvRow)

        except Exception as e:
            pass
        finally:
            csvFile.close()
            