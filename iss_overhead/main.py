import datetime
import sys
import pytz
import requests
import smtplib
import os
from email.message import EmailMessage
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import time
# ignore insecure request warning because api owner didn't bother to update the certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# coordinates of current city
dejon_lat = 36.3301010
dejon_long = 127.4224700
# date in the current city in year-month-day format
date = datetime.date.today().strftime("%Y-%m-%d")

def is_overhead():
    # get ISS's current position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_data = response.json()
    iss_position = iss_data.get("iss_position")
    iss_longitude = eval(iss_position.get("longitude"))
    iss_latitude = eval(iss_position.get("latitude"))
    # end get ISS's current position
    return abs(iss_longitude - dejon_long) < 5 and abs(iss_latitude - dejon_lat) < 5


# Get sunrise/sunset times
response = requests.get(
    url=f"https://api.sunrise-sunset.org/json?lat={dejon_lat}&lng={dejon_long}&date={date}&formatted=0",
    verify=False)

time_data = response.json()["results"]

# convert UTC time to Asia/Seoul time
for key, value in time_data.items():
    if key == "sunrise" or key == "sunset":
        utc_datetime = datetime.datetime.strptime(time_data[key], "%Y-%m-%dT%H:%M:%S%z")
        utc_datetime.replace(tzinfo=pytz.UTC)
        adjusted_datetime = datetime.datetime.astimezone(utc_datetime, tz=pytz.timezone("Asia/Seoul"))
        time_data[key] = adjusted_datetime.time()

# get current time
time_in_dejon = datetime.datetime.now().time()


def is_night():
    return time_data["sunset"].hour < time_in_dejon.hour < time_data["sunrise"].hour


# # login credentials
gmail = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_APP")
gmail_smtp = "smtp.gmail.com"

# message object with sender/recipient data
msg = EmailMessage()
msg["From"] = gmail
msg["To"] = gmail

while True:
    # if it's night
    if is_night():
        # and if ISS is overhead
        if is_overhead():
            # create email message
            msg["Subject"] = "ISS overhead!"
            msg.set_content("ISS is overhead! Go outside and see it.")
            break
    else:
        print("Poor visibility during the day. Check again at night")
        sys.exit(0)
    print("ISS not overhead yet\nwait for 60 seconds...\n")
    time.sleep(60)
    print("Checking again...")

with smtplib.SMTP(gmail_smtp, 587) as connection:
    # start a secure TSL connection
    connection.ehlo()
    connection.starttls()
    connection.ehlo()

    # login and send the mail
    connection.login(gmail, password)
    connection.send_message(msg)
