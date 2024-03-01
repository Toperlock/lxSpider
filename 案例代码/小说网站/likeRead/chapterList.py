#解析整本书的章节名及章节地址

from lxml import etree
import requests
import chapter
import query
import json

HEADER = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

with open('static/rules.json', 'r', encoding='utf-8')as fp:
    rules = json.load(fp)

#判断网站，识别运行哪一种解析规则
def classify(url):
    for web in rules:
        if rules[web]["realm"] == "":rules[web]["realm"] = url
    webName = url.split(".")[1]
    begin = False
    for i in rules:
        if webName == i:
            begin = True
    if begin:return analysis(webName,url)
    else:
        print("链接错误或暂不支持该网站，可前往论坛反馈，要求楼主添加！！！")
        return


#进行解析，获取章节名和章节链接
def analysis(webName,url):
    html = etree.HTML(requests.get(url,HEADER).content.decode(rules[webName]['code'],errors='ignore'))
    title = html.xpath(rules[webName]['title'])
    title = [t for t in title if '\xa0' not in t]
    urlList = html.xpath(rules[webName]['urlList'])
    book_name = html.xpath(rules[webName]['book_name'])[0].strip()
    #判断，判断该小说是否保存过
    query_all = query.query(book_name,title,urlList,False)
    store_old = []
    if query_all:
        print("该小说已保存至（%s），请选择："%query_all["title"][0])
        print("1、原文件继续保存")
        print("2、与旧章节分开保存")
        queryTF = input("请输入序号选择：")
        if queryTF == "1":
            title = query_all["title"]
            urlList = query_all["urlList"]
            store_old = query_all["store"]
        else:
            query_all = query.query(book_name,title,urlList,True)
    if webName == 'xbiquge': # xbiquge 的最新章节舍去，按需修改 注：中断后需去掉索引值才能与原文件继续保存
        title = title[:]
    print("小说名称：%s"%book_name)
    print("小说章节：%d章"%(len(title)+len(store_old)))
    print("已存章节：%d章"%len(store_old))
    if input("是否开始保存？(y/n)：") == "n":return
    print("-----开始保存-----")
    realm = rules[webName]['realm']
    store_all = []
    for i in range(len(title)): # xbiquge 的最新章节舍去，按需修改 注：中断后需去掉索引值才能与原文件继续保存
        if webName == 'piaotia':
            store = {
                "title":title[i].strip(),
                "urlList":url+urlList[i]
            }
        elif webName == 'xbiquge':
            store = {
                "title":title[i].strip(), # xbiquge 的最新章节舍去，按需修改 注：中断后需去掉索引值才能与原文件继续保存
                "urlList":url+urlList[i]
            }
        elif webName == 'xbiquzw':
            store = {
                "title":title[i].strip(), # xbiquge 的最新章节舍去，按需修改 注：中断后需去掉索引值才能与原文件继续保存
                "urlList":url+urlList[i]
            }
        else:
            store = {
                "title":title[i].strip(),
                "urlList":realm+urlList[i]
            }
        store_all.append(store)
    chapter.classify(book_name,webName,store_all,store_old)
