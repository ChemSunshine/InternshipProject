from tkinter import *
import datetime
import weathermap

def k_to_f(k):
    return round((k - 273.15) * 9/5 + 32)

def uvi_to_colors(uvi):
    if (uvi <= 2):
        return ("green", "black")
    if (uvi <= 5):
        return ("yellow", "black")
    if (uvi <= 8):
        return ("orange", "black")
    if (uvi <= 10):
        return ("red", "white")
    return ("violet", "black")

COLUMN_WIDTH = 22

class WeatherCell(Frame):
    def __init__(self, root, daily):
        super().__init__(root)

        time = datetime.datetime.fromtimestamp(daily["dt"])
        self.weekday = Label(self, width=COLUMN_WIDTH, text=time.strftime("%A"))
        self.weekday.grid(column=0, row=0)

        weather = daily["weather"][0]
        self.image = weathermap.get_weather_image(weather["icon"], 75)
        weather_frame = Frame(self)
        image_label = Label(weather_frame, image=self.image)
        image_label.grid()
        image_description = Label(weather_frame, text=weather["description"], width=COLUMN_WIDTH)
        image_description.grid()
        weather_frame.grid(column=1, row=0)

        min_temp = k_to_f(daily["temp"]["min"])
        self.min = Label(self, text=min_temp, width=COLUMN_WIDTH)
        self.min.grid(column=2, row=0)

        max_temp = k_to_f(daily["temp"]["max"])
        self.max = Label(self, text=max_temp, width=COLUMN_WIDTH)
        self.max.grid(column=3, row=0)

        uvi = daily["uvi"]
        uvi_colors = uvi_to_colors(uvi)
        self.uvi = Label(self, text=uvi, width=COLUMN_WIDTH, bg=uvi_colors[0], fg=uvi_colors[1])
        self.uvi.grid(column=4, row=0)


