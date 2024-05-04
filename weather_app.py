from dotenv import load_dotenv
import os
import requests
import math

load_dotenv()

API_KEY=os.getenv("API_KEY")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_units():
    units = None
    while True:
        try:
            print('1 - Imperial (F)')
            print('2 - Metric (C)')
            print('3 - Standard (K)')
            units = int(input("Select a unit of measurement (1-3): "))
            if 1 <= units <= 3:
                return units
            else:
                cls()
                print(f'Error: {units} is not a valid option')
                print("Please select option 1, 2, or 3.\n")
        except ValueError:
            cls()
            print('Error: Input is not an integer')
            print("Please select option 1, 2, or 3.\n")

selected_units = get_units()

if selected_units == 1:
    api_units = 'imperial'
    temperature_units = 'F'
elif selected_units == 2:
    api_units = 'metric'
    temperature_units = 'C'
elif selected_units == 3:
    api_units = 'standard'
    temperature_units = 'K'

city = input('Search for a city: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={api_units}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = math.ceil(data['main']['temp'])
    desc = data['weather'][0]['description']
    print(f'Temperature: {temperature} {temperature_units}')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')