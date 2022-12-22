from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

category = {
            '水泥': '食品',
            '食品': '塑膠',
            '塑膠': '紡織',
            '紡織': '電機',
            '電機': '電器電纜',
            '電器電纜': '化學',
            '化學': '生技',
            '生技': '玻璃',
            '玻璃': '造紙',
            '造紙': '鋼鐵',
            '鋼鐵': '橡膠',
            '橡膠': '汽車',
            '汽車': '半導體',
            '半導體': '電腦週邊',
            '電腦週邊': '光電',
            '光電': '通訊網路',
            '通訊網路': '電子零組件',
            '電子零組件': '電子通路',
            '電子通路': '資訊服務',
            '資訊服務': '其他電子',
            '其他電子': '營建',
            '營建': '航運',
            '航運': '觀光',
            '觀光': '金融業',
            '金融業': '貿易百貨',
            '貿易百貨': '油電燃氣',
            '油電燃氣': '存託憑證',
            '存託憑證': 'ETF',
            'ETF': '受益證券',
            '受益證券': 'ETN',
            'ETN': '創新板',
            '創新板': '其他',
            '其他': '指數類',
}

url = f'https://tw.stock.yahoo.com/class-quote?sectorId=1&exchange=TAI'
PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)
driver.get(url)

for a in category:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, f"上市類股 / {a}"))
    )
    get_ok = driver.find_element(By.LINK_TEXT, f"上市類股 / {a}")
    time.sleep(1)
    get_ok.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, category[a]))
    )

    ok = driver.find_element(By.LINK_TEXT, category[a])
    time.sleep(1)
    ok.click()

