
import smtplib, os, datetime, random
from email.message import EmailMessage
import pandas as pd

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
tday = datetime.date.today()
day_now = tday.day
month_now = tday.month

names = []
emails = []

# Password and email (from environment variable)
gmail = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_APP")
gmail_server = "smtp.gmail.com"

for birthday in birthdays.iterrows():

    if birthday[1]["month"] == month_now and birthday[1]["day"] == day_now:
        names.append(birthday[1]["name"])
        emails.append(birthday[1]["email"])

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
for i in range(len(names)):
    template_index = random.choice([1,2,3])
    template = f"letter_templates/letter_{template_index}.txt"
    with open(template, "r+") as f:
        data = f.read()
        letter = data.replace("[NAME]", f"{names[i]}")

    # set email message
    msg = EmailMessage()
    msg["Subject"] = "Happy birthday!"
    msg["From"] = gmail
    msg["To"] = emails[i]
    msg.set_content(letter)

# 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP(gmail_server, 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()

        connection.login(gmail, password)
        connection.send_message(msg)
    msg.clear()
