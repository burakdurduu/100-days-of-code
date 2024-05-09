import requests
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = os.environ.get("API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

daily_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY, 
}

news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "language": "en",
}


stock_response = requests.get(STOCK_ENDPOINT, params=daily_params)
daily_data = stock_response.json()["Time Series (Daily)"]

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]
first_3_articles = articles[0:3]
formatted_articles = [f"Headline: {value['title']}\nBrief: {value['description']}\n\n" for value in first_3_articles]

closing_stock_list = [value["4. close"] for (key, value) in daily_data.items()]
yesterday_csp = float(closing_stock_list[0])
before_yesterday_csp = float(closing_stock_list[1])
difference = (yesterday_csp - before_yesterday_csp)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_diff = round((difference / yesterday_csp) * 100)
string_articles = ""
if abs(percentage_diff) > 5:  # Set diff here.
    for i in range(3):
        string_articles += formatted_articles[i]
    
    subject = f"{STOCK_NAME}:{up_down}{percentage_diff}%"
    body = string_articles
    message = EmailMessage()
    message.add_header("From", MY_EMAIL)
    message.add_header("To", MY_EMAIL)
    message.add_header("Subject", subject)
    message.set_payload(body, "utf-8")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(message, from_addr=MY_EMAIL, to_addrs=MY_EMAIL)
