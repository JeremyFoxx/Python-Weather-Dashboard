import tkinter as tk
from tkinter import messagebox, Entry, Label, Button, Radiobutton, StringVar
import requests

# Constants
API_KEY = '81b9dbca42b478c1868f0571891fd257'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}'

# Function to fetch weather data
def fetch_weather(city, units):
    url = BASE_URL.format(city, API_KEY, units)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"Cannot find city: {city}")
        return None

# Function to display weather data
def display_weather(data, units):
    try:
        name = data['name']
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        unit_symbol = '°C' if units == 'metric' else '°F'

        results.config(text=f'City: {name}\nTemperature: {temp} {unit_symbol}\nCondition: {weather}')
    except Exception as e:
        messagebox.showerror("Error", f"Error retrieving data: {e}")

# Function to initiate a search
def search():
    city = city_entry.get()
    units = units_var.get()
    weather_data = fetch_weather(city, units)
    if weather_data:
        display_weather(weather_data, units)

# GUI setup
root = tk.Tk()
root.title("Weather Dashboard")

units_var = StringVar(value='metric')  # default unit

# Entry for city name
Label(root, text="Enter City:", font=('Helvetica', 12)).pack(pady=10)
city_entry = Entry(root, justify='center', width=20, font=('Helvetica', 18))
city_entry.pack(pady=5)
city_entry.focus_set()

# Unit selection
Radiobutton(root, text='Celsius', variable=units_var, value='metric').pack()
Radiobutton(root, text='Fahrenheit', variable=units_var, value='imperial').pack()

# Button to fetch weather
Button(root, text="Get Weather", command=search, font=('Helvetica', 12)).pack(pady=20)

# Label to display results
results = Label(root, text="", font=('Helvetica', 14))
results.pack(pady=20)

root.mainloop()