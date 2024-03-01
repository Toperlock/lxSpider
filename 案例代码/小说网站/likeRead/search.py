import requests as rts
from bs4 import BeautifulSoup as Bp
import re

def reqdata(key,url):
    r = rts.post(url,{'searchkey':key})
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def handledata(key,url):
    re_list = []
    soup = Bp(reqdata(key,url),'html.parser')
    data = soup.find_all('a')
    for i in data:
        try:
            if re.findall(key,i.text): #根据关键字进行筛选
                '''if i['href'][:4] == 'http':
                    re_list.append(i.text + ':' + i['href'])'''
                re_list.append(i.text + ':' + i['href'])
        except:
            continue

    if len(re_list):
        for j in range(len(re_list)):
            print(str(j)+":"+re_list[j])
        print("-"*50)
        print("请复制下载链接到方框内下载")
    else:
        print('未找到相关小说')

def search(name):
    key = name
    #url = "https://www.xbiquge.la/modules/article/waps.php"
    url = "https://www.xbiqugu.info/modules/article/waps.php"
    handledata(key,url)
