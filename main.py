import requests


def get_weather(city_name):
    url = ''.join([
        'https://api.openweathermap.org/data/2.5/weather?q=',
        str(city_name),
        '&appid=404b51a2b0365e05382a9c72d4848868&units=metric',
    ])

    data = requests.get(url).json()

    print(data['name'], '-', data['weather'][0]['description'], '\n',
          'Temperature: ', data['main']['temp'], '°C', '\n',
          'Humidity: ', data['main']['humidity'], '%', '\n',
          'Wind Speed: ', data['wind']['speed'], 'metre/sec', '\n',
          'Wind Direction:', data['wind']['deg'], 'degrees'
          )


if __name__ == '__main__':
    print(f"This python script tells you the weather of a given city.")
    print(f"Please key in a city name:")
    city = str(input())
    get_weather(city)
