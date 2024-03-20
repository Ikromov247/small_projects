import requests
import os
from twilio.rest import Client

will_rain: bool

weather_params = {
    "appid": "",
    "lat": 36.3504,
    "lon": 127.3845
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather", params=weather_params)
data = response.json()

weather_code = 1000
for weather in data["weather"]:
    weather_code = weather["id"]

temperature = round(data["main"]["temp"] - 273, 2)

will_rain = False
if weather_code < 700:
    will_rain = True

account_sid = os.environ['TWILIO_ID']
auth_token = os.environ['TWILIO_TOKEN']

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Bring an umbrella. It's going to rain today(┬┬﹏┬┬)",
        from_='+12057549884',
        to='+821021157720'
    )

    # print(message._properties)
