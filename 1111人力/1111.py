from requests import get
from bs4 import BeautifulSoup
from openpyxl import Workbook
from time import sleep

wbTitle = ['連結', '徵求', '公司名稱', '位置', '薪水']

wb = Workbook()
ws = wb.create_sheet("1111人力銀行", 0)

ws.append(wbTitle)

URL='https://www.1111.com.tw/search/job?ks=%E9%9F%8C%E9%AB%94&page='

page = 1

res=get(url=URL+str(page))

soup=BeautifulSoup(res.text,"html.parser")

while soup.find_all('div',class_="job_item_info")!=[]:
    print('正在爬取第',page,'頁')
    for job in soup.find_all('div',class_="job_item_info"):
        title = job.h5.text
        commpany = job.h6.text
        url = job.a['href']
        location = job.find_all('a',class_="job_item_detail_location mr-3 position-relative")[0].text
        salary = job.find_all('div', class_="job_item_detail_salary ml-3 font-weight-style digit_6")[0].text
        ws.append([url,title,commpany,location,salary])
    page += 1
    URL2 = URL + str(page)
    res = get(url=URL2)
    soup = BeautifulSoup(res.text, "html.parser")
    sleep(1)
wb.save('111人力銀行.xlsx')
