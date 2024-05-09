import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

zillow_link = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=zillow_link)
data = response.text
soup = BeautifulSoup(data, "html.parser")

address_list = []
address_elements = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
for element in address_elements:
    address_text = element.getText()
    address = address_text.strip().replace("|", "")
    address_list.append(address)


price_list = []
price_elements = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
for element in price_elements:
    price_text = element.getText()
    price = price_text[:6].replace("+", "")
    price_list.append(price)


link_list = []
link_elements = soup.find_all("a", class_="property-card-link")
for element in link_elements:
    link = element.get("href")
    link_list.append(link)

# Selenium
form_url = "https://forms.gle/Ro3rHimW3Q1UoSU28"
chrome_path = r"/Users/burakdurdu/Downloads/chromedriver-mac-arm64/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(form_url)

for i in range(len(price_list)):
    time.sleep(3)
    address_entry = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                        '2]/div/div[1]/div/div[1]/input')
    address_entry.send_keys(f"{address_list[i]}")
    price_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
    price_entry.send_keys(f"{price_list[i]}")
    link_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                               '1]/div/div[1]/input')
    link_entry.send_keys(f"{link_list[i]}")
    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    send_button.click()
    send_again_button = driver.find_element(By.CSS_SELECTOR, value=".c2gzEf a")
    send_again_button.click()
driver.quit()
