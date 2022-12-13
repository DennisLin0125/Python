import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from time import sleep

wbTitle = ['類別', '股票名稱', '代號', '股價', '漲跌', '漲跌幅', '開盤', '昨收', '最高', '最低', '成交量(張)', '時間', '連結']

category = {
            '水泥': 1, '食品': 2, '塑膠': 3, '紡織': 4, '電機': 6, '電器電纜': 7, '化學': 37, '生技': 38,
            '玻璃': 9, '造紙': 10, '鋼鐵': 11, '橡膠': 12, '汽車': 13, '半導體': 40, '電腦週邊': 41, '光電': 42,
            '通訊網路': 43, '電子零組件': 44, '電子通路': 45, '資訊服務': 46, '其他電子': 47, '營建': 19, '航運': 20, '觀光': 21,
            '金融業': 22, '貿易百貨': 24, '油電燃氣': 39, '存託憑證': 25, 'ETF': 26, '受益證券': 29, 'ETN': 48, '創新板': 49,
            '其他': 30, '市認購': 31, '市認售': 32, '指數類': 33, '市牛證': 51, '市熊證': 52
}

wb = Workbook()
ws = wb.create_sheet("yahoo即時股價", 0)

ws.append(wbTitle)

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
          }
sumL = 0
for page in category:
    類別 = page
    print(f'正在爬取 {類別} 頁')
    url = f'https://tw.stock.yahoo.com/class-quote?sectorId={category[類別]}&exchange=TAI'
    web = requests.get(url, headers=headers)  # 取得網頁內容
    soup = BeautifulSoup(web.text, "html.parser")  # 轉換內容
    all_data = soup.find_all('div', class_='Bgc(#fff) table-row D(f) H(48px) Ai(c) Bgc(#e7f3ff):h Fz(16px) Px(12px) Bxz(bb) Bdbs(s) Bdbw(1px) Bdbc($bd-primary-divider)')
    a = 0
    for stock in all_data:
        if len(stock.find_all('div', class_='Lh(20px) Fw(600) Fz(16px) Ell')) >= 1:
            股票名稱 = stock.find_all('div', class_='Lh(20px) Fw(600) Fz(16px) Ell')[0].text
        elif len(stock.find_all('div', class_='Lh(20px) Fw(600) Fz(14px) Ell')) >= 1:
            股票名稱 = stock.find_all('div', class_='Lh(20px) Fw(600) Fz(14px) Ell')[0].text

        股票代號 = stock.find_all('span', class_='Fz(14px) C(#979ba7) Ell')[0].text

        連結 = f'https://tw.stock.yahoo.com/quote/{股票代號}'

        股價 = stock.find_all('span', class_='Jc(fe)')[0].text
        股價Temp = 股價.replace(',', '')
        開盤 = stock.find_all('span', class_='Jc(fe)')[3].text
        昨收 = stock.find_all('span', class_='Jc(fe)')[4].text
        昨收Temp = 昨收.replace(',', '')
        最高 = stock.find_all('span', class_='Jc(fe)')[5].text
        最低 = stock.find_all('span', class_='Jc(fe)')[6].text
        成交量 = stock.find_all('span', class_='Jc(fe)')[7].text

        if 股價 != '-':
            漲跌 = f'{float(股價Temp)-float(昨收Temp):.2f}'
            漲跌幅 = f'{float(漲跌)/float(昨收Temp)*100:.2f}%'
        else:
            漲跌 = 最高
            漲跌幅 = 最高

        時間 = stock.find_all('div', class_='Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(48px)')[0].text

        ws.append([類別, 股票名稱, 股票代號, 股價, 漲跌, 漲跌幅, 開盤, 昨收, 最高, 最低, 成交量, 時間, 連結])
        a += 1
    sumL += a
    print(f'共 {a} 筆完成')
    print('＝＝＝＝＝＝＝＝＝＝＝＝＝')
    sleep(1)
print(f'全部 {sumL} 筆完成')
wb.save('yahoo股價.xlsx')
