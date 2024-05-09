from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_path = r"/Users/burakdurdu/Downloads/chromedriver-mac-arm64/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument(f"--user-data-dir=/Users/burakdurdu/Library/Application Support/Google/Chrome/")
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref=cm_r_cp_ud_ct_FM9M699VKHTT47YD58Q6&th-1")
# time.sleep(10)
# price_in_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_in_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is {price_in_cents.text}.{price_in_cents.text}")

# driver.get("https://www.python.org/")
# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul a")
#
# events = {}
# for i in range(len(event_names)):
#     events[i] = {
#         "time": event_times[i].text,
#         "name": event_names[i].text,
#     }
# print(events)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, value=("#articlecount a"))
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# driver.quit()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CSS_SELECTOR, "form button")
first_name.send_keys("Burak")
last_name.send_keys("Durdu")
email.send_keys("example@gmail.com")
button.click()
time.sleep(3)
driver.quit()
