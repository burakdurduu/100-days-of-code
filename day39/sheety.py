import requests
import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.environ.get("SHEETY_API_USERNAME")
AUTH = os.environ.get("SHEETY_AUTH")
URL = "https://api.sheety.co"
PROJECT = "flightDeals"
SHEET = "users"


def new_user():
    first_name = input("What is your first name: \n>")
    last_name = input("What is your last name: \n>")
    email = input("What is your email: \n>")
    email2 = input("Type your email again: \n>")


# if email in sheety: return false

print("Welcome to Burak's Flight Club. \nWe find the best flight deals and email you.")