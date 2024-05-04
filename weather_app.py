from dotenv import load_dotenv
import os
import requests
import math

load_dotenv()

API_KEY=os.getenv("API_KEY")

city = input('Search for a city: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    desc = data['weather'][0]['description']
    fahrenheit = math.ceil(1.8 * (temperature - 273) + 32) 
    print(f'Temperature: {fahrenheit} F')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')