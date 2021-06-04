import requests
import geocoder
import json
from PIL import Image, ImageTk

def get_weather_data():
    location = geocoder.ip('me')
    g = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid=a79a323fbca764cdddfa0316d394a226".format(location.lat, location.lng))
    weather_data = json.loads(g.content)
    return weather_data

def get_weather_image(iconName: str, size=50):
    im = Image.open("images/{}@2x.png".format(iconName))
    return ImageTk.PhotoImage(im.resize((size, size)))