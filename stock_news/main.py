import re
import requests
import os
from twilio.rest import Client
import datetime
import sys

# api tokens and keys
sms_api_id = 1
sms_api_token = ""
news_apikey = ""
stock_apikey = ""

# json stock data keys for getting time series, opening and closing prices
time_series = "Time Series (Daily)"
opening = "1. open"
closing = "4. close"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
need_news = False
is_weekday = False
msg_body = ""

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": stock_apikey
}
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
data = stock_response.json()


def get_dates() -> tuple[str, str]:
    global is_weekday
    # get today's and yesterday's dates, format as 2000-12-31
    date_format = "%Y-%m-%d"
    time_delta = datetime.timedelta(days=1)
    tday = datetime.date.today() - time_delta
    yesterday = (datetime.date.today() - time_delta)

    # if today's weekend do nothing
    if tday.weekday() == 6 or tday.weekday() == 5:
        print("Today's the weekend. No stocks")
        is_weekday = False
        sys.exit(0)

    # if monday set friday date as yesterday's
    elif tday.weekday() == 0:
        yesterday = yesterday - 3 * time_delta

    # format dates as string 2012-12-31
    tday = tday.strftime(date_format)
    yesterday = yesterday.strftime(date_format)
    is_weekday = True
    return tday, yesterday


tday_date, yesterday_date = get_dates()

if is_weekday:
    # get today's opening and yesterday's closing prices
    today_opening = eval(data[time_series][tday_date][opening])
    yesterday_closing = eval(data[time_series][yesterday_date][closing])
    # difference_percentage = round((today_opening-yesterday_closing) / 100, 1)
    difference_percentage = 10

    print(today_opening, yesterday_closing, difference_percentage)

    if abs(difference_percentage) > 5:
        need_news = True
    else:
        sys.exit(0)
    difference_symbol = "up" if difference_percentage > 0 else "down"

# # STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if need_news:
    news_paramaters = {
        "q": "Tesla",
        "language": 'en',
        "apiKey": news_apikey
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything?", params=news_paramaters)
    news_response.raise_for_status()
    news_data = news_response.json()

    if news_data["status"] == "ok" and len(news_data["articles"]) > 0:
        # random.shuffle(top_articles)
        top_articles = news_data["articles"]
        msg_body = f"~\n\n{STOCK} {difference_symbol} {difference_percentage}%\n" \
                   f"Last closing: ${yesterday_closing}\n" \
                   f"Today's opening: ${today_opening}\n"
        count = 0
        for top_article in top_articles:
            headline = top_article["title"]
            temp = top_article["description"]
            snippet = re.sub(r"<a .+</a>", "", temp)
            link = top_article["url"]
            msg_body += f"\nHeadline: {headline}\nBrief: {snippet}\n-->{link}\n\n"

            count += 1
            if count == 3:
                break

    elif len(news_data["articles"]) == 0 or news_data["status"] == "error":
        msg_body = f"~\n\n{STOCK} {difference_symbol} {difference_percentage}%\n" \
                   f"Last closing: ${yesterday_closing}\n" \
                   f"Today opening: ${today_opening}\n" \
                   f"No headlines for today"

# # STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

client = Client(sms_api_id, sms_api_token)
message = client.messages \
    .create(
    body=msg_body.strip(),
    from_='+',
    to='+'
)
