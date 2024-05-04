# Weather App

## Overview
This is a simple weather app built using Python. It provides users with current weather information based on their location or a specified location.

## Planned Features
- **Current Weather:** Display current weather conditions including temperature, humidity, wind speed, etc.
- **Location-Based:** Automatically fetch weather information based on the user's location using geolocation services.
- **Search by Location:** Allow users to search for weather information by entering a specific location.

## Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create an account or sign into an existing one on [OpenWeather](https://openweathermap.org/)
4. Navigate to your API keys and generate a key
5. Create a .env file in your cloned repository parent directory (under ./weather-app)
6. Copy your key from OpenWeather and paste it into a variable named API_KEY in your .env file

Example .env file, line 1:

    API_KEY = PASTEYOURKEYHERE
    
7. Run the `weather_app.py` file using Python.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
