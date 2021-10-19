import requests
from pprint import pprint

_API_KEY = 'Your weather id '


def getWeather(cityName):
    '''Function for getting weather information with city name
    * cityName is value of city name for getting informating

    Example : cityName = 'London'
    '''
    base_url = f'https://api.openweathermap.org/data/2.5/weather?appid={_API_KEY}&q={cityName}'

    weatherData = requests.get(base_url).json()
    
    pprint(weatherData)
    

getWeather('Tashkent')

