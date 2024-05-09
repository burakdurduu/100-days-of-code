import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.trendyol.com/duxweel/apple-macbook-air-mly33tu-a-m2-13-6-inch-premium-su-ve-toz-gecirmez-tasima-cantasi-p-377443423?boutiqueId=61&merchantId=153891&utm_source=aff_t&utm_medium=cpc&utm_campaign=akakce_urun_listeleme&v=1.64"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

headers = {
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Defined",
}
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price_span = soup.find(name="span", class_="prc-dsc")
price_text = price_span.getText().split(",")[0]
price = int(price_text)
if price < 800:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Discount\n\nNew Bag Price:{price}TL\n{URL}",
        )
