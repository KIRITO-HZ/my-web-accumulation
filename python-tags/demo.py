# -*- coding: utf-8 -*-

import requests
# 正则
import re
# 系统
import os
# 文件操作
import codecs

def get_title(url):
    s = requests.session()
    h = s.get(url)
    html = h.content.decode('utf-8')
    #print html

    qurl = '<a href="/2018/01/04/first-exploration-electron-2/">(.*?)</a>'
    qurllist = re.findall(qurl,html)
    #print qurllist


    for each in qurllist:
        f = codecs.open("result.txt", 'a', 'utf-8')
        f.write(each+'\n')
        print each
        #f.flush()
        f.close()

for i in range(1,1000):
    url = 'http://jartto.wang/page/'+str(i)+'/'
    get_title(url)