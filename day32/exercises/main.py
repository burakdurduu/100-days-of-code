import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
adress = ""

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt")as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

if weekday == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(
            from_addr=my_email,
            to_addrs=adress,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


# smtp.gmail.com / smtp.live.com / smtp.mail.yahoo.com

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=adress,
        msg="Subject:Hello\n\nThis is the body of my email"
    )

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
