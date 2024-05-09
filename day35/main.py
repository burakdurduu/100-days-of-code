import requests
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

url = "https://api.openweathermap.org/data/2.8/onecall?"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": 41.0026,
    "lon": 39.7167,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url, params=weather_params)
response.raise_for_status()
weather_data = response.json()

for i in range(0, 12):
    weather_id = weather_data["hourly"][i]["weather"][0]["id"]
    if weather_id < 700:
        subject = f"Rain Alert 🌧️🌧️"
        body = f"Bring an Umbrella ☔"
        message = EmailMessage()
        message.add_header("Subject", subject)
        message.set_payload(body, "utf-8")
        
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.send_message(
                from_addr=my_email,
                to_addrs=my_email,
                msg=message
            )
            print("Mail Sended.")
        break
