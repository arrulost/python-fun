import requests
from twilio.rest import Client # type: ignore

account_sid = 'your account sid'
auth_token = 'your auth token'
client = Client(account_sid, auth_token)

api_key = "your api key"

parameters = {
    "lat":44.42,
    "lon":26.14,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

def check_weather(num):
    if num < 700:
        return True
    else:
        return False

for item in weather_data["hourly"][:12]:
    if check_weather(item["weather"][0]["id"]):
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella ☔.",
        from_='your twilio number',
        to='your actual number'
        )

        print(message.sid)
    

