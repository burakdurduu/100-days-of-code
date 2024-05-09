from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_path = "/Users/burakdurdu/Downloads/chromedriver-mac-arm64/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
service = Service(chrome_path)
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get("http://secure-retreat-92358.herokuapp.com")
firts_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
e_mail = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CLASS_NAME, value="btn")
firts_name.send_keys("Burak")
last_name.send_keys("Durdu")
e_mail.send_keys("example@gmail.com")
button.click()
