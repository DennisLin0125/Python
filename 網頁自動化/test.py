from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

Option = webdriver.ChromeOptions()
prefs = {
            "profile.default_content_setting_values":
            {
                "notifications": 2
            }
}
Option.add_experimental_option('prefs', prefs)

PATH = "./chromedriver"
driver = webdriver.Chrome(PATH, options=Option)
driver.get("https://www.facebook.com")

帳號 = ''
密碼 = ''

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[id="email"]')))
username.send_keys(帳號)
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[id="pass"]')))
password.send_keys(密碼)

enter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[name="login"]')))
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

soup = BeautifulSoup(driver.page_source, "html.parser")

print(soup.prettify())
#enter.click()
