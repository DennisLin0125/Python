import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from time import sleep

wbTitle = ['連結','股票名稱', '代號', '股價', '漲跌', '漲跌幅','開盤','昨收','最高','最低','成交量(張)','時間']
pages = ['1','2','3','4','6','7','37','38','9','10','11','12','13','40','41','42','43','44','45','46'
         ,'47','19','20','21','22','24','39','25','26','29','48','49','30','31','32','33','51','52']

wb = Workbook()
ws = wb.create_sheet("yahoo即時股價", 0)

temUrl='https://tw.stock.yahoo.com.tw/quote/'

ws.append(wbTitle)
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
sum = 0
for page in pages:
    print('正在爬取第', page, '頁')
    url = f'https://tw.stock.yahoo.com/class-quote?sectorId={page}&exchange=TAI'
    web = requests.get(url,headers=headers)  # 取得網頁內容
    soup = BeautifulSoup(web.text, "html.parser")  # 轉換內容
    all_data = soup.find_all('div',class_='Bgc(#fff) table-row D(f) H(48px) Ai(c) Bgc(#e7f3ff):h Fz(16px) Px(12px) Bxz(bb) Bdbs(s) Bdbw(1px) Bdbc($bd-primary-divider)')
    a = 0
    for stock in all_data:
        if len(stock.find_all('div',class_='Lh(20px) Fw(600) Fz(16px) Ell'))>=1:
            股票名稱=stock.find_all('div',class_='Lh(20px) Fw(600) Fz(16px) Ell')[0].text
        elif len(stock.find_all('div',class_='Lh(20px) Fw(600) Fz(14px) Ell'))>=1:
            股票名稱 = stock.find_all('div', class_='Lh(20px) Fw(600) Fz(14px) Ell')[0].text

        股票代號=stock.find_all('span', class_='Fz(14px) C(#979ba7) Ell')[0].text
        連結 = temUrl + 股票代號
    #===================================股價============================================================
        股價=stock.find_all('span', class_='Jc(fe)')[0].text
    #=====================================漲跌==============================================================
        if len(stock.find_all('span', class_='Fw(600) Jc(fe) D(f) Ai(c)'))>=1:
            # stock_up_down = stock.find_all('span', class_='Fw(600) Jc(fe) D(f) Ai(c)')[0].text
            # stock_up_down_pricent = stock.find_all('span', class_='Fw(600) Jc(fe) D(f) Ai(c)')[1].text
            漲跌 = stock.find_all('span', class_='Jc(fe)')[1].text
            漲跌幅 = stock.find_all('span', class_='Jc(fe)')[2].text
        elif len(stock.find_all('span', class_='Fw(600) Jc(fe) D(f) Ai(c) C($c-trend-up)'))>=1:
            # stock_up_down = '+' + stock.find_all('span', class_='Mend(4px) Bds(s)')[0].next.text
            # stock_up_down_pricent = '+' + stock.find_all('span', class_='Mend(4px) Bds(s)')[1].next.text
            漲跌 = '+' + stock.find_all('span', class_='Jc(fe)')[1].text
            漲跌幅 = '+' + stock.find_all('span', class_='Jc(fe)')[2].text
        elif len(stock.find_all('span', class_='Fw(600) Jc(fe) D(f) Ai(c) C($c-trend-down)')) >= 1:
            # stock_up_down = '-' + stock.find_all('span', class_='Mend(4px) Bds(s)')[0].next.text
            # stock_up_down_pricent = '-' + stock.find_all('span', class_='Mend(4px) Bds(s)')[1].next.text
            漲跌 = '-' + stock.find_all('span', class_='Jc(fe)')[1].text
            漲跌幅 = '-' + stock.find_all('span', class_='Jc(fe)')[2].text

        開盤 = stock.find_all('span', class_='Jc(fe)')[3].text
        昨收 = stock.find_all('span', class_='Jc(fe)')[4].text
        最高 = stock.find_all('span', class_='Jc(fe)')[5].text
        最低 = stock.find_all('span', class_='Jc(fe)')[6].text
        成交量 = stock.find_all('span', class_='Jc(fe)')[7].text

        時間=stock.find_all('div', class_='Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(48px)')[0].text

        ws.append([連結, 股票名稱, 股票代號, 股價, 漲跌, 漲跌幅, 開盤, 昨收, 最高, 最低, 成交量, 時間])
        a += 1
    sum += a
    print('共',a,'筆完成')
    print('＝＝＝＝＝＝＝＝＝＝＝＝＝')
    sleep(1)
print('全部', sum, '筆完成')
wb.save('yahoo股價.xlsx')