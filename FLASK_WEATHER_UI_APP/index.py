from dotenv import load_dotenv
from pprint import pprint

import requests
import os

load_dotenv() #Load the data From the .env file and fetch it the api_key

def get_current_weather (city="Tamil Nadu") :
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'
    
    weather_data = requests.get(request_url).json()
    
    return weather_data #Return as a JSON Data

if __name__ == "__main__" :
    print("\n**** Get Current Weather Conditions *** \n")
    
    city = input("\n Please enter a city name : ")
    
    #Check for empty string or string with only spaces
    if not bool(city.strip()) :
        city = "Tamil Nadu"
    
    weather_data = get_current_weather (city)
    
    print("\n")
    pprint(weather_data)