import requests
from dotenv import load_dotenv
import os

load_dotenv()

def weather_application () :
    api_key = os.getenv("API_KEY")

    try :
        print("***** REAL TIME WEATHER APPLICATION *****")
        print("")
        city = input("ENTER THE CITY NAME : ").upper()
        print("")

        weather_api = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q" : city,
            "appid" : api_key,
            "units" : "metric"
        }

        response = requests.get(weather_api, params=params)
        data = response.json()

        print("*"*30)
        print()

        print(f"CITY NAME IS : {data["name"].upper()}")
        print(f"TEMPERATURE NAME IS : {data["main"]["temp"]}")
        print(f"WEATHER CONDITIONS : {data["weather"][0]["main"].upper()}")
        
        print()
        print("*"*30)

    except Exception as error:
        print(f"Error : {error}")

weather_application()