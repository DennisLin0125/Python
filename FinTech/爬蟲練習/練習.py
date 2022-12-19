# -*- coding: UTF-8 -*-

import urllib.request as httplib  # 3.x

#  SSL  處理，  https    SSSSSS 就需要加上以下2行
import ssl
ssl._create_default_https_context = ssl._create_unverified_context    # 因.urlopen發生問題，將ssl憑證排除

headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

url = "https://tw.stock.yahoo.com/class-quote?sectorId=1&exchange=TAI"

req = httplib.Request(url, data=None, headers=headers) #連線

reponse = httplib.urlopen(req)               # 開啟連線動作
if reponse.code == 200:                        # 當連線正常時
    contents = reponse.read()                  # 讀取網頁內容
    contents = contents.decode("utf-8")        # 轉換編碼為 utf-8
    print(contents)