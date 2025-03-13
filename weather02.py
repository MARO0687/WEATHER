import requests
from dotenv import load_dotenv
import os
#clase para obtener el clima de una ciudad
class Clima:
    def __init__(self):
        load_dotenv()
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.api_key = os.getenv('API_KEY')

    def consulta_ciudad(self,ciudad):
        params = {
            'q': ciudad,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        return response.json()
#requests.get('http://api.openweathermap.org/data/2.5/weather?q=Toluca&appid=API_KEY&units=metric')
c=Clima()
print(c.consulta_ciudad('Toluca'))
print(c.consulta_ciudad('Tokyo'))
print(c.consulta_ciudad('Paris'))