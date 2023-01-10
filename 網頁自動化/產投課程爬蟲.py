from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from openpyxl import Workbook
from bs4 import BeautifulSoup
from openpyxl import Workbook

titles = ['訓練班別 (訓練單位)', '課程代碼', '訓練人數', '訓練時數', '學員負擔',
          '政府負擔', '學科/術科 訓練地點', '報名開始', '報名結束', '招生狀態',
          '訓練開始', '訓練結束', '繳費方式', '網址']

wb = Workbook()
ws = wb.create_sheet('課程', 0)

ws.append(titles)

PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://ojt.wda.gov.tw/ClassSearch/ClassSch2")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "buttons"))
)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()  # 按下ESC

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'PagingInfo_PageSize'))
)

# select = Select(driver.find_element_by_id('PagingInfo_PageSize'))
select = Select(driver.find_element(By.ID, value='PagingInfo_PageSize'))

select.select_by_index(0)  # 下拉選單選擇(全部)

# get_ok=driver.find_element_by_id("btnGoRecCount")
get_ok = driver.find_element(By.ID, value="btnGoRecCount")

get_ok.click()

time.sleep(2)

pageSource = driver.page_source
soup = BeautifulSoup(pageSource, "html.parser")
driver.quit()

i = 0
j = 1
for data in soup.find_all('tr'):
    if i >= 6:
        連結 = 'https://ojt.wda.gov.tw' + data.select('a')[1]['href']
        訓練班別 = data.select('a')[0].text.replace('\n', '  ')
        課程代碼 = data.select('td')[2].text
        訓練人數 = data.select('td')[3].text
        訓練時數 = data.select('td')[4].text
        學員負擔 = data.select('td')[5].text
        政府負擔 = data.select('td')[6].text
        訓練地點 = data.select('td')[7].text.replace('\n', '')
        報名開始 = data.select('td')[8].text[:19].replace('\n', '')
        報名結束 = data.select('td')[8].text[37:55]
        招生狀態 = data.select('td')[9].text
        訓練開始 = data.select('td')[10].text[:10].replace(' ', '')
        訓練結束 = data.select('td')[10].text[28:].replace(' ', '')
        繳費方式 = data.select('td')[11].text
        ws.append([訓練班別, 課程代碼, 訓練人數, 訓練時數, 學員負擔, 政府負擔,
                   訓練地點, 報名開始, 報名結束, 招生狀態, 訓練開始, 訓練結束,
                   繳費方式, 連結])
        print(f'第 {j} 筆完成')
        j += 1
    i += 1
wb.save('訓練課程.xlsx')
