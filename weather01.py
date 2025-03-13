import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        #Para cambiar la ciudad, cambiar el valor de 'q' por la ciudad deseada (Ej. 'q': 'Toluca')
        'q': city,
        #Mando a llamar mi api_key
        'appid': api_key,
        #Para cambiar la unidad de temperatura, cambiar el valor de 'units' por 'imperial' (Fahrenheit) o 'metric' (Celsius)
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

#requests.get('http://api.openweathermap.org/data/2.5/weather?q=Toluca&appid=API_KEY&units=metric')

city = 'Toluca'
weather_data = get_weather(api_key, city)
print(weather_data)