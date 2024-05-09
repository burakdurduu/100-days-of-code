import smtplib
from email.message import EmailMessage
import datetime as dt
import pandas as pd
import random
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict.keys():
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:  
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"].capitalize())

    subject = f"Happy Birthday 🎂🎂"
    body = contents
    message = EmailMessage()
    message.add_header("Subject", subject)
    message.set_payload(body, "utf-8")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # for gmail
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.send_message(
            from_addr=EMAIL, 
            to_addrs=birthday_person["email"],
            msg=message
        )
