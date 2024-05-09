import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 187
AGE = 31
# Nutritionix
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
# Sheety
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
API_USERNAME = os.environ.get("API_USERNAME")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()

today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.strftime("%X")

sheet_endpoint = f"https://api.sheety.co/{API_USERNAME}/myActivities/page1"

for exercise in result["exercises"]:
    sheet_inputs = {
        "page1": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD))
print(f"{sheet_response.text}\n\nAll information is saved on your Google Sheets")
