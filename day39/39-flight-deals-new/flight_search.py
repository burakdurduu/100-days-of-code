import os
import requests
from dotenv import load_dotenv
load_dotenv()


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self.KIWI_LOCATIONS_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
        self.KIWI_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        self.headers = {
            "apikey": os.environ.get("KIWI_API_KEY")
        }
        self.iata_code = ""

    def get_iata_code(self, city_name):
        params = {
            "term": city_name
        }
        response = requests.get(self.KIWI_LOCATIONS_ENDPOINT, params=params, headers=self.headers)
        response.raise_for_status()
        self.iata_code = response.json()["locations"][0]["code"]
        return self.iata_code

    def search_flights(self, fly_from, fly_to, date_from, date_to):
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to
        }
        response = requests.get(self.KIWI_SEARCH_ENDPOINT, params=params, headers=self.headers)
        response.raise_for_status()
        flights = response.json()
        return flights
