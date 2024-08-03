import requests
import datetime as dt
my_latitude = 32.085369
my_longitude = 72.674980
response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()
longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']

parameter = {
    'lat': my_latitude,
    'lng': my_longitude,
    'formatted': 0
}

response_sun_set = requests.get('https://api.sunrise-sunset.org/json', params=parameter)
response_sun_set.raise_for_status()
res = response_sun_set.json()
sunrise = (res['results']['sunrise'].split('T'))[1].split(':')[0]
sunset = (res['results']['sunset'].split('T'))[1].split(':')[0]

today = dt.datetime.now()
print(today.hour)


print(sunrise)