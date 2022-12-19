import requests
from bs4 import BeautifulSoup

category = {'ETF': 26}

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

arr = []
for data in category:
    print(f'正在爬取 {data} 頁')
    url = f'https://tw.stock.yahoo.com/class-quote?sectorId={category[data]}&exchange=TAI'
    web = requests.get(url, headers=headers)  # 取得網頁內容
    soup = BeautifulSoup(web.text, "html.parser")  # 轉換內容
    #all_data = soup.select('ul')[16].select('li')
    all_data = soup.find_all('ul')[16].find_all('li',class_="List(n)")
    for i in all_data:
        a = i.contents[0].contents
        for j in a:
            arr.append(j.text)
        k+=1
        print(arr)
        arr = []
    print(f'共{k}筆')