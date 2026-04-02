import requests
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()

def get_current_weather () :
    print('**** GET CURRENT WEATHER CONDITIONS ****\n')

    city = input("PLEASE ENTER A CITY NAME : \n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    #print(request_url)

    weather_data =  requests.get(request_url).json()
    #pprint(weather_data)

    print(f"CURRENT WEATHER FOR {weather_data["name"]}.\n")
    print(f"TEMPERATURE IS  {weather_data["main"]["temp"]}.\n")
    print(f"FEELS LIKE IS  {weather_data["main"]["feels_like"]} AND {weather_data["weather"][0]["description"].upper()}.")

if __name__ == "__main__" :
    get_current_weather()