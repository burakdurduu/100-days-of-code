import os
import requests
from dotenv import load_dotenv

load_dotenv()
SHEETY_API_USERNAME = os.environ.get('SHEETY_API_USERNAME')
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
USERNAME = os.environ.get("SHEETY_USERNAME")
PASSWORD = os.environ.get("SHEETY_PASSWORD")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_api_endpoint = f"https://api.sheety.co/{SHEETY_API_USERNAME}/flightDeals/prices"
        self.sheety_headers = {
            "Authorization": SHEETY_AUTH
        }
        self.row = 2
        self.data = None
        self.city_list = []

    def get_sheety_data(self):
        response = requests.get(url=self.sheety_api_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        self.data = response.json()
        return self.data

    def get_city_list(self):
        self.city_list = [data["city"] for data in self.data["prices"]]
        return self.city_list

    def put_iata_code(self, city_iata_code):
        sheety_put_endpoint = f"https://api.sheety.co/287a69b3bb587f5c85aaefc314cfaded/flightDeals/prices/{self.row}"
        self.row += 1
        sheety_inputs = {
            "price": {
                "iataCode": city_iata_code,
            }
        }
        iata_list = [data["iataCode"] for data in self.data["prices"]]
        for iata in iata_list:
            if iata == "":
                response = requests.put(url=sheety_put_endpoint, headers=self.sheety_headers, json=sheety_inputs, auth=(USERNAME, PASSWORD))
                response.raise_for_status()
