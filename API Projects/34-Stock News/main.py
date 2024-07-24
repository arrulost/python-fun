import requests
from twilio.rest import Client # type: ignore

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = 'twilio account sid'
auth_token = 'twilio auth token'
client = Client(account_sid, auth_token)

api_key = "stock api key"
news_api_key = "news api key"

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key
}

news_parameters = {
    "q":COMPANY_NAME,
    "apiKey": news_api_key
}


response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()

yesterday = '2024-07-22'
day_before_yesterday = '2024-07-19'

yesterdays_closing_price = [data['4. close'] for date, data in stock_data["Time Series (Daily)"].items() if date == yesterday][0]
day_before_yesterday_price = [data['4. close'] for date, data in stock_data["Time Series (Daily)"].items() if date == day_before_yesterday][0]



difference = float(yesterdays_closing_price) - float(day_before_yesterday_price)
up_down = None
if difference >0:
    up_down ="🔺"
else:
    up_down= "🔻"
percentage = round((difference/float(yesterdays_closing_price)) * 100)


if abs(percentage) > 1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()
    first_3_articles = news["articles"][:3]
    formmatted_articles = [f"{STOCK_NAME}{up_down}{percentage}%\n:Headline: {article['title']}. \nBrief: {article['description']}" for article in first_3_articles]
    for article in formmatted_articles:
        message = client.messages.create(
                body=article,
            from_='your twilio number',
            to='your number'
            )



