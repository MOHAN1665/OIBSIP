import requests
from tkinter import Tk, Label, Entry, Button, Frame, StringVar, messagebox

API_KEY = '8752c6ebfe5ab01006a2b3b168e53acf'  # Your API Key here

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        weather = data['weather'][0]['description'].capitalize()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        return (f"Temperature: {temp}°C\n"
                f"Feels Like: {feels_like}°C\n"
                f"Min Temp: {temp_min}°C\n"
                f"Max Temp: {temp_max}°C\n"
                f"Weather: {weather}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s\n"
                f"Wind Direction: {wind_deg}°")
    else:
        return "Failed to retrieve weather data. Check your API key and subscription."

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    weather_info = get_weather(city)
    result_var.set(weather_info)

# GUI Setup
root = Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Header Frame
header_frame = Frame(root, bg="#007bff", pady=10)
header_frame.pack(fill="x")

header_label = Label(header_frame, text="Weather App", font=("Helvetica", 18, "bold"), fg="white", bg="#007bff")
header_label.pack()

# Main Content Frame
content_frame = Frame(root, bg="#f0f0f0", padx=20, pady=20)
content_frame.pack(pady=10)

Label(content_frame, text="Enter City:", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=5)
city_entry = Entry(content_frame, font=("Helvetica", 14))
city_entry.pack(pady=5)

Button(content_frame, text="Get Weather", font=("Helvetica", 14), bg="#007bff", fg="white", command=show_weather).pack(pady=10)

result_var = StringVar()
result_label = Label(content_frame, textvariable=result_var, font=("Helvetica", 12), bg="#f0f0f0", justify="left")
result_label.pack()

root.mainloop()
