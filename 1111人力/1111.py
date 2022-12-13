from requests import get
from bs4 import BeautifulSoup
from openpyxl import Workbook

wbTitle = ['連結', '職缺', '公司名稱', '地點', '薪水']

wb = Workbook()
ws = wb.create_sheet("1111人力銀行", 0)

ws.append(wbTitle)

page = 1

URL = f'https://www.1111.com.tw/search/job?ks=%E9%9F%8C%E9%AB%94&page={page}'

res = get(URL)

soup = BeautifulSoup(res.text, "html.parser")

job_data = soup.find_all('div', class_="job_item_info")

sumL = 0

while job_data:
    print('正在爬取第', page, '頁')
    a = 0
    for job in job_data:
        職缺 = job.h5.text
        公司名稱 = job.h6.text
        連結 = job.a['href']
        地點 = job.find_all('a', class_="job_item_detail_location mr-3 position-relative")[0].text
        薪水 = job.find_all('div', class_="job_item_detail_salary ml-3 font-weight-style digit_6")[0].text
        ws.append([連結, 職缺, 公司名稱, 地點, 薪水])
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
wb.save('111人力銀行.xlsx')
