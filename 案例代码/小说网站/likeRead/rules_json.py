import json

rules = {
    "piaotia":{
        "title":'//div[@class="centent"]/ul/li//text()', #2024.2.29修改
        "urlList":'//div[@class="centent"]/ul/li/a/@href',
        "book_name":'//div[@class="title"]/h1/text()',
        "realm":"https://www.piaotia.com/",
        "chapter":'//text()', #迫不得已操作
        "code":"gbk"
    },
    "xbiquge":{
        "title":'//div[@id="list"]//dd//text()', #2024.2.29修改
        "urlList":'//div[@id="list"]//dd/a/@href',
        "book_name":'//div[@id="info"]//h1/text()',
        "realm":"http://www.xbiquge.bz/",
        "chapter":'//div[@id="content"]/text()',
        "code":"gbk"
    },
    "xbiqugu":{
        "title":'//div[@id="list"]//dd//text()', #2024.2.29修改
        "urlList":'//div[@id="list"]//dd/a/@href',
        "book_name":'//div[@id="info"]//h1/text()',
        "realm":"http://www.xbiqugu.info/",
        "chapter":'//div[@id="content"]/text()',
        "code":"utf-8"
    },
    'xbiquzw':{
        "title":'//div[@id="list"]//dd//text()', #2024.3.1修改
        "urlList":'//div[@id="list"]//dd//a/@href',
        "book_name":'//div[@id="info"]//h1/text()',
        "realm":"http://www.xbiquzw.com/",
        "chapter":'//div[@id="content"]//text()',
        "code":"utf-8"
    },
    '51shucheng':{
        "title":'//div[@class="mulu-list"]//li//text()',
        "urlList":'//div[@class="mulu-list"]//li//a/@href',
        "book_name":'//div[@class="catalog"]//h1/text()',
        "realm":"https://www.51shucheng.net/",
        "chapter":'//div[@class="neirong"]//text()',
        "code":"utf-8"
    }
}
with open('./static/rules.json', 'w', encoding='utf-8') as fp:
    json.dump(rules, fp, ensure_ascii=False)
