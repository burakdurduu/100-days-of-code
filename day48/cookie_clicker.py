from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_path = r"/Users/burakdurdu/Downloads/chromedriver-mac-arm64/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument(f"--user-data-dir=/Users/burakdurdu/Library/Application Support/Google/Chrome/")
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5

while True:
    cookie.click()
    money_element = driver.find_element(By.ID, "money").text
    if "," in money_element:
        money_element = money_element.replace(",", "")
    money = int(money_element)
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices_list = []
        for price in all_prices:
            try:
                cost = (int(price.text.split("-")[1].strip().replace(",", "")))
                prices_list.append(cost)
            except IndexError:
                pass
        for i in prices_list[::-1]:
            if money >= i:
                try:
                    all_prices[prices_list.index(i)].click()
                    break
                except IndexError:
                    pass
        timeout = time.time() + 5
