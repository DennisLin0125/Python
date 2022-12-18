from requests import post
from bs4 import BeautifulSoup
from openpyxl import Workbook

wbTitle = ['課程名稱', '課程代碼', '訓練人數', '時數', '學員負擔', '政府負擔', '地點', '報名日期', '招生狀態'
           , '訓練日期', '繳費方式', '課程連結']

wb = Workbook()
ws = wb.create_sheet("產投課程表", 0)

ws.append(wbTitle)

fd = {
    'Form.PlanType': '1',
    'Form.OCID': None,
    'Form.KEYWORDS': '大數據',
    'Form.CLASSCNAME': None,
    'Form.CASETYPE': '0',
    'Form.STDATE_YEAR_SHOW': '111',
    'Form.STDATE_MON': '11',
    'Form.FTDATE_YEAR_SHOW': '112',
    'Form.FTDATE_MON': '3',
    'Form.TEACHCNAME': None,
    'Form.COMIDNO': None,
    'Form.CTID': None,
    'Form.ZIPCODE': None,
    'Form.SCHOOLNAME': None,
    'Form.ORGKIND': None,
    'Form.CLASSCATE': None,
    'Form.JOBTMID': None,
    'Form.TMID': None,
    'Form.TGOVEXAM': None,
    '__SECURITY_FORM_ID__': 'SamMyLLbRCK55eaTDHOSLGVdQ9vhtPoaFYumv5M48yE='
}

URL = f'https://ojt.wda.gov.tw/ClassSearch'

res = post(URL, fd)
soup = BeautifulSoup(res.text,"html.parser")

for i in range(10):
    all_data = soup.find_all('tr', valign='middle')[i]

    課程名稱 = all_data.find('td', headers="tb1-b").a.text
    連結 = all_data.find('td', headers="tb1-b").select('a')[1]['href']
    課程連結 = f'https://ojt.wda.gov.tw/{連結}'
    課程代碼 = all_data.find('td', headers="tb1-c").text
    訓練人數 = all_data.find('td', headers="tb1-d").text
    時數 = all_data.find('td', headers="tb1-e").text
    學員負擔 = all_data.find('td', headers="tb1-f tb1-f1").text
    政府負擔 = all_data.find('td', headers="tb1-f tb1-f2").text
    地點 = all_data.find('td', headers="tb1-g").text
    報名日期 = all_data.find('td', headers="tb1-i").text
    招生狀態 = all_data.find('td', headers="tb1-j").text
    訓練日期 = all_data.find('td', headers="tb1-k").text
    繳費方式 = all_data.find('td', headers="tb1-l").text
    ws.append([課程名稱, 課程代碼, 訓練人數, 時數, 學員負擔, 政府負擔, 地點,
               報名日期, 招生狀態, 訓練日期, 繳費方式, 課程連結])
wb.save('產投課程表.xlsx')