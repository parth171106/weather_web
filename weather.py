import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def current_weather(city="Surat"):
   

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data=requests.get(request_url).json()

    #pprint(weather_data)
    return weather_data
   
    
if __name__=="__main__":
    print("\n*** Get Current Weather ***\n")
    city = input("\nPlease enter a city name:\n")

    if not bool(city.strip()):
        city="Surat"

    weather_data = current_weather(city) 
    pprint(weather_data)

