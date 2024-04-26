import regeyquest

token = '6223b9bb1c7800cfb61153c4405f954d'
city = 'Tashkent'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

response = requests.get(url)

if response.status_code == 200:

    data = response.json()
     = data['weather'][0]['description']
     = data['main']['temp']
    print(f"Weather in {city}: {weather_description}, Temperature: {temperature}K")
else:
    print("Error in getting data:", response.status_code)
