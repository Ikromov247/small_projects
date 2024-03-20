# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
import requests

cheap_deals = []
flights = FlightSearch()
data_mngr = DataManager()
sms = NotificationManager()

users = data_mngr.get_users()


for city in data_mngr.cities:
    temp = flights.get_flight_deal(city["iataCode"])
    if len(temp["data"]) > 0:
        flight_deal = FlightData(temp)
    else:
        continue
    print(flight_deal.price, flight_deal.fly_to,flight_deal.booking_link, flight_deal.duration)
    if int(city["lowestPrice"]) > flight_deal.price:
        cheap_deals.append(flight_deal)
        print("deal found")


def shorten_link(link):
    api_key = "254dcf805714f072b6d2389706bc2dfe20fb544f"
    endpoint = "https://api-ssl.bitly.com/v4/shorten"
    parameters = {
        "group_id": "Bm8o9zav6Lr",
        "domain": "bit.ly",
        "long_url": link
    }
    header = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(url=endpoint, json=parameters, headers=header).json()
    return response["link"]


if len(cheap_deals) > 0:
    users = data_mngr.get_users()

    for cheap_deal in cheap_deals:
        booking_link = shorten_link(cheap_deal.booking_link)
        body = f"`\nLow price alert! Only {cheap_deal.price} to fly " \
               f"from {cheap_deal.fly_from}-{cheap_deal.fly_from_code} to " \
               f"{cheap_deal.fly_to}-{cheap_deal.fly_to_code} on {cheap_deal.departure}\n\n" \
               f"Book now here: {booking_link}"

        for user in users:
            full_name = user["firstName"] + " " + user["lastName"]
            e_mail = user["email"]
            sms.send_email(e_mail, body + f"\n\nsent to {full_name}")
        # status = sms.send_message(body)
else:
    print("No deal found, yet")
