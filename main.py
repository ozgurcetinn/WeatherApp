import requests
import json

API_KEY = 'd60919342a63a57c3892b96541a8ae7a'


def fetch_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={API_KEY}&q={city}"
    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None


def display_weather_data(weather_data):
    if weather_data:
        if weather_data['cod'] != '404':
            main_data = weather_data['main']
            # Convert from Kelvin to Celsius
            humidity = main_data['humidity']
            temperature = main_data['temp'] - 273.15
            weather_description = weather_data['weather'][0]['description']

            print(f"Temperature: {temperature:.2f}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather description: {weather_description.capitalize()}")
        else:
            print("City not found. Please try again.")
    else:
        print("Failed to retrieve weather data.")


def main():
    city = input("Enter the name of the city: ")
    weather_data = fetch_weather_data(city)
    display_weather_data(weather_data)


if __name__ == "__main__":
    main()
