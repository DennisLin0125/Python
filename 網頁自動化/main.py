from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from openpyxl import Workbook

titles = ['訓練班別 (訓練單位)', '課程代碼', '訓練人數', '訓練時數', '學員負擔', '政府負擔', '學科/術科 訓練地點','報名日期','招生狀態','預訂訓練 起迄日期','繳費方式','網址']

wb = Workbook()
ws = wb.create_sheet('課程', 0)

ws.append(titles)

PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://ojt.wda.gov.tw/ClassSearch/ClassSch2")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"buttons"))
)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()   #按下ESC


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID,'PagingInfo_PageSize'))
)

#select = Select(driver.find_element_by_id('PagingInfo_PageSize'))
select = Select(driver.find_element(By.ID,value='PagingInfo_PageSize'))

select.select_by_index(0) #下拉選單選擇(全部)

#get_ok=driver.find_element_by_id("btnGoRecCount")
get_ok=driver.find_element(By.ID,value="btnGoRecCount")

get_ok.click()

time.sleep(2)

Non_titles=['','課程名稱：','開訓日期間','查詢條件','課程代碼：',"課程收藏 課程比一比","輔導考證： 不拘",'縣市別：全部(全部)','單位名稱：全部','訓練業別：全部']

arr=[]
i=0
num=0
#tds=driver.find_elements_by_tag_name('td')
tds=driver.find_elements(By.TAG_NAME,value='td')

for td in tds:
    if td.text in Non_titles:
        continue    
    elif td.text[:5]=='開訓日期間':
        continue
    arr.append(td.text)
    i+=1
    if i>10:
        arr.append("https://ojt.wda.gov.tw/ClassSearch/Detail?PlanType=1&OCID="+arr[1])
        ws.append(arr)
        num += 1
        arr = []
        i=0
        print('第 '+str(num)+' 筆完成')
wb.save('訓練課程.xlsx')
driver.quit()


