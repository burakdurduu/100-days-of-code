import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
rows_data = []

base_url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/"
for i in range(4):
    if i == 0:
        url = base_url
    else:
        url = base_url + f"page/{i}"
    driver.get(
        url=url)
    x = driver.find_elements(By.CLASS_NAME, value="data-table__value")
    if i == 0:
        time.sleep(30)
    else:
        time.sleep(10)
    t = 0
    row_data = []
    for a in x:
        row_data.append(a.text.replace("$", "").replace("%", ""))
        t += 1
        if t % 6 == 0:
            rows_data.append(row_data)
            row_data = []
print(rows_data)
# driver.quit()

heading = ["Rank:", "Major:", "DegreeType:", "EarlyCareerPay:", "Mid-CareerPay:", "%HighMeaning:"]

for x in rows_data:
    print(x)
    for y in range(len(x)):
        x[y] = x[y].replace(",", "")
        if x[y] == "-":
            x[y] = 0
print(rows_data)
df = pd.DataFrame(data=rows_data, columns=heading)
df.to_csv("college_salary_current_data.csv", index=False)
