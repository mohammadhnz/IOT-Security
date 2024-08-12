import requests


def get_weather(api_key, city):
    """Fetches weather information for a specified city using the OpenWeather API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Parsing some details from the response
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        print(f"Current temperature: {temperature} °C")
        print(f"Weather: {weather_description}")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Failed to get weather data, status code: {response.status_code}")
        print("Response message:", response.text)


# Replace 'your_api_key_here' with your OpenWeather API key
api_key = 'b0e08b1044b3d76434d9ffb9daf03ff0'
city = 'Tehran'  # Specify the city

get_weather(api_key, city)
