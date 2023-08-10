import tkinter as tk
import requests
import tkinter.messagebox

def get_weather_data(location):
    api_key = "ecb8f73dcc33bd561b915f25990e3559"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather_info = {
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Wind Speed": data["wind"]["speed"],
            "Description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return None

def get_weather():
    location = entry_location.get()
    weather_data = get_weather_data(location)

    if weather_data:
        weather_text.delete("1.0", tk.END)
        for key, value in weather_data.items():
            weather_text.insert(tk.END, f"{key}: {value}\n")
    else:
        tkinter.messagebox.showerror("Error", "Weather information not found. Please check the location.")

root = tk.Tk()
root.title("Weather Forecast")

label_location = tk.Label(root, text="Enter the name of a city or a zip code:")
entry_location = tk.Entry(root)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)

weather_text = tk.Text(root, height=10, width=40)

label_location.pack()
entry_location.pack()

get_weather_button.pack()

weather_text.pack()

root.mainloop()