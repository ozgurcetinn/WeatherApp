import requests
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

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

            result_text.set(f"Temperature: {temperature:.2f}°C\n"
                            f"Humidity: {humidity}%\n"
                            f"Weather description: {weather_description.capitalize()}")
        else:
            result_text.set("City not found. Please try again.")
    else:
        result_text.set("Failed to retrieve weather data.")

def get_weather():
    city = city_entry.get()
    weather_data = fetch_weather_data(city)
    display_weather_data(weather_data)

# Create the main window
screen = Tk()
screen.title("Weather App")
screen.minsize(width=500, height=400)

# Load the background image
background_image = Image.open("weather.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas and place the background image on it
canvas = Canvas(screen, width=500, height=400)
canvas.pack(expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Create and place the widgets on the canvas
welcome_label = Label(screen, text="Welcome! Please Enter The City:", font=("Arial", 15), bg="white")
canvas.create_window(250, 50, window=welcome_label)

# Entry for city
city_entry = Entry(screen, width=40)
canvas.create_window(250, 100, window=city_entry)

# Use StringVar for result text
result_text = StringVar()
result_label = Label(screen, textvariable=result_text, width=30, height=5, font="15")
canvas.create_window(250, 200, window=result_label)

# Get Weather button
get_weather_button = Button(screen, text="Get Weather", font=("Arial", 15), command=get_weather)
canvas.create_window(250, 300, window=get_weather_button)

# Start the Tkinter event loop
screen.mainloop()
