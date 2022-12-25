from requests import get
from bs4 import BeautifulSoup
from openpyxl import Workbook

wbTitle = ['連結', '職缺', '公司名稱', '工作地點', '縣市', '鄉鎮市區', '薪水', '給薪方式', '薪資下限', '薪資上限', '薪資平均']

wb = Workbook()
ws = wb.create_sheet("1111人力銀行", 0)

ws.append(wbTitle)

page = 1

URL = f'https://www.1111.com.tw/search/job?ks=%E9%9F%8C%E9%AB%94&page={page}'

res = get(URL)

soup = BeautifulSoup(res.text, "html.parser")

job_data = soup.find_all('div', class_="job_item_info")

sumL = 0

def 地點轉換(local):

    縣市 = local[:3]

    鄉鎮市區 = local.replace(縣市, '')

    return 縣市, 鄉鎮市區

def 薪資轉換(e):

    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '萬', '~', '.']

    price = ''

    給薪方式 = e[:2]

    if 給薪方式 == '面議':
        a = e.find('年')
        if a == -1:
            給薪方式 = f'(月薪)面議'
        else:
            給薪方式 = f'(年薪)面議'


    for char in e:
        if char in arr:
            price += char

    if '~' in price:
        薪資下限 = price[:price.find('~')]
        薪資上限 = price[price.find('~')+1:]
    else:
        薪資上限 = price
        薪資下限 = price


    if '萬' in 薪資上限:
        薪資上限 = float(薪資上限.replace('萬',''))*10000
    else:
        薪資上限 = float(薪資上限)

    if '萬' in 薪資下限:
        薪資下限 = float(薪資下限.replace('萬',''))*10000
    else:
        薪資下限 = float(薪資下限)

    薪資平均=(薪資下限+薪資上限)/2

    return 給薪方式, 薪資上限, 薪資下限, 薪資平均

#while job_data:
print('正在爬取第', page, '頁')
a = 0
for job in job_data:
    職缺 = job.h5.text
    公司名稱 = job.h6.text
    連結 = job.a['href']
    地點 = job.find_all('a', class_="job_item_detail_location mr-3 position-relative")[0].text
    地點 = 地點.replace('台', '臺')
    縣市, 鄉鎮市區 = 地點轉換(地點)
    薪水 = job.find_all('div', class_="job_item_detail_salary ml-3 font-weight-style digit_6")[0].text
    給薪方式, 薪資上限, 薪資下限, 薪資平均 = 薪資轉換(薪水)
    ws.append([連結, 職缺, 公司名稱, 地點, 縣市, 鄉鎮市區, 薪水, 給薪方式, 薪資下限, 薪資上限, 薪資平均])
    a += 1
sumL += a
page += 1
print('共', a, '筆')
print('======================')
URL = f'https://www.1111.com.tw/search/job?ks=%E9%9F%8C%E9%AB%94&page={page}'
res = get(URL)
soup = BeautifulSoup(res.text, "html.parser")
job_data = soup.find_all('div', class_="job_item_info")
print('共', sumL, '個職缺')
wb.save('111人力銀行-1.xlsx')


