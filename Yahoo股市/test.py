import requests
from bs4 import BeautifulSoup

category = {'ETF': 26}

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

arr = []

for data in category:
    k = 0
    print(f'正在爬取 {data} 頁')
    url = f'https://tw.stock.yahoo.com/class-quote?sectorId={category[data]}&exchange=TAI'
    html = requests.get(url, headers=headers)  # 取得網頁內容
    soup = BeautifulSoup(html.text, "html.parser")  # 轉換內容
    for all_data in soup.find_all('li',class_='List(n)'):
        連結 = all_data.find('a')['href']
        代號 = 連結.replace('https://tw.stock.yahoo.com/quote/','')
        arr.append(代號)
        for a in all_data.contents[0].contents:
            arr.append(a.text)
        k += 1
        arr.append(連結)
        股價 = arr[2]
        昨收 = arr[6]
        漲跌 = arr[3]
        漲跌幅 = arr[4]
        if 股價 != '-':
            if float(股價) - float(昨收) > 0:
                arr[3] = f'△{漲跌}'
                arr[4] = f'△{漲跌幅}'
            elif float(股價) - float(昨收) < 0:
                arr[3] = f'▽{漲跌}'
                arr[4] = f'▽{漲跌幅}'

        arr[1] = arr[1].replace(代號, '')
        print(arr)

        arr = []

    print(f'共{k}筆')