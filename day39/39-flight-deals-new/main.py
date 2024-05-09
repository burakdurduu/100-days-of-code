import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flight_search import FlightSearch
from data_manager import DataManager
MY_LOCATION = "IST"

dm = DataManager()
fs = FlightSearch()
data = dm.get_sheety_data()
city_list = dm.get_city_list()

for city in city_list:
    dm.put_iata_code(fs.get_iata_code(city))
    fly_from = fs.get_iata_code(MY_LOCATION)
    fly_to = fs.get_iata_code(city)
    today = datetime.now().strftime("%d/%m/%Y")
    three_months_later = (datetime.now() + relativedelta(months=+3)).strftime("%d/%m/%Y")
    flights_data = fs.search_flights(fly_from, fly_to, today, three_months_later)

    # requests.exceptions.HTTPError: 402 Client Error: Payment Required
