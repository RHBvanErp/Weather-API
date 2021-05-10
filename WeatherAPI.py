import tkinter as tk
import requests
import time
 

def getWeather(canvas):
    label1.config(text = "Invalid input", bg = "red")
    label2.config(text = "Please try again", bg = "red")

    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition  + "\n"+ str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "  |  " + "Max Temp: " + str(max_temp) + "°C" + "\n" + "\n" + "Pressure: " + str(pressure) + "  |  " +"Humidity: " + str(humidity) + "\n" + "\n" +"Wind Speed: " + str(wind) + "\n" + "\n" + "Sunrise: " + sunrise + "  |  " + "Sunset: " + sunset
    label1.config(text = final_info,bg = "blue",fg = "white")
    label2.config(text = final_data,bg = "blue",fg = "white")


canvas = tk.Tk()
canvas.geometry("500x400")
canvas.title("Weather-Checker")
canvas.configure(background= "blue")
f = ("Times", 15)
t = ("Times", 20, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t, text = "Welcome to Wheather-Checker",bg = "blue",fg = "white")
label2 = tk.Label(canvas, font=f, text = "Please type in the location you want information of \n in the textbox above",bg = "blue",fg = "white")
label1.pack()
label2.pack()
canvas.mainloop()
