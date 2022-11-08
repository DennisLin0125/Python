import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time

wbTitle = ['股票', '代號', '即時股價', '漲跌', '漲跌(%)', '成交量', '成交', '開盤',
           '最高', '最低', '均價', '成交值(億)', '昨收', '昨量', '振幅', '內盤', '外盤', '本益比 (同業平均)', '時間']
wb = Workbook()
ws = wb.create_sheet("當日股票資訊", 0)
ws.append(wbTitle)
print(wbTitle)

stock_num = ['0050', '0056', '2317', '2330', '2302', '2454', '2303', '1303', '2301', '2324', '2367', '3008',
            '2409', '3481', '3049', '2002', '3105', '2603', '2609', '2615', '2618', '2610','2344']
urlString = 'https://tw.stock.yahoo.com/quote/'
urls = []
for x in stock_num:
    urls.append(urlString + x)

i = 0
wsArr = []

for url in urls:
    web = requests.get(url)  # 取得網頁內容
    soup = BeautifulSoup(web.text, "html.parser")  # 轉換內容
    stock_title = soup.find('h1', class_='C($c-link-text) Fw(b) Fz(24px) Mend(8px)')  # 找到 h1 的內容

    source = soup.find('div', class_='D(f) Ai(fe) Mb(4px)')
    price = source.contents[0].text  # 股價
    up_down_price = source.contents[1].text  # 漲跌
    price_percent = source.contents[2].text  # 百分比

    amount = soup.find_all('span', class_='Fz(16px) C($c-link-text) Mb(4px)')[0]  # 成交量
    Ratio = soup.find_all('span', class_='Fz(16px) C($c-link-text) Mb(4px)')[1]  # 本益比 (同業平均)

    data = soup.find('ul', class_='D(f) Fld(c) Flw(w) H(192px) Mx(-16px)')
    mynumbers = [i for i in range(12)]
    dataArr = []
    for mynum in mynumbers:
        if mynum == 7 or mynum == 8 or mynum == 9:  # 跳過漲跌,漲跌幅,百分比
            continue
        dataArr.append(((data.contents[mynum]).contents[1]).get_text())     # 獲取細節Table資料
    
    disk=soup.find('div', class_='D(f) Jc(sb) Ai(c) Mb(4px) Fz(16px)--mobile Fz(14px)')
    indisk_price=disk.contents[0].next.next_sibling.contents[0]     #內盤
    #indisk_price_percent = (disk.contents[0].next.next_sibling.contents[1]).get_text()

    outdisk_price=disk.contents[1].next.contents[0]  #外盤
    #outdisk_price_percent = (disk.contents[1].next.contents[1]).get_text()

    tem_class = ''
    class_Len = len(source.next.attrs['class'])
    if class_Len == 7:
        tem_class = source.next.attrs['class'][6]
    elif class_Len == 9:
        tem_class = source.next.attrs['class'][8]

    symbol = ''  # 漲或跌的狀態
    if tem_class == "C($c-trend-down)":
        symbol = '▽'
    elif tem_class == "C($c-trend-up)":
        symbol = '△'
    elif tem_class == "Bgc($c-trend-up)":
        symbol = '▲'

    local_time = time.localtime()  # 取得時間元組
    timeString = time.strftime("%Y/%m/%d %H:%M", local_time)  # 轉成想要的字串形式

    wsArr.append(stock_title.get_text())
    wsArr.append(stock_num[i])
    wsArr.append(price)
    wsArr.append(symbol + up_down_price)
    wsArr.append(symbol + price_percent)
    wsArr.append(amount.get_text())

    wsArr.extend(dataArr) # 將細節資料加入wsArr

    wsArr.append(indisk_price)
    #wsArr.append(indisk_price_percent)
    wsArr.append(outdisk_price)
    #wsArr.append(outdisk_price_percent)

    wsArr.append(Ratio.get_text())
    wsArr.append(timeString)

    print(wsArr)
    ws.append(wsArr)
    wsArr = []
    i += 1
wb.save('即時股票資訊.xlsx')
