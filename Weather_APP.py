import pip._vendor.requests
import json
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = pip._vendor.requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        city = weather_data["name"]
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
    else:
        print("Error retrieving weather data. Please check the city name or API key.")

if __name__ == "__main__":
    API_KEY = "enter_api_key_here" #API key
    city_name = input("Enter city name: ")
    weather = get_weather(city_name, API_KEY)
    display_weather(weather)
