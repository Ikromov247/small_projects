from twilio.rest import Client
import smtplib
from email.message import EmailMessage
import os

sms_api_id = os.environ.get("TWILIO_ID")
sms_api_token = os.environ.get("TWILIO_TOKEN")
my_gmail = os.environ.get("EMAIL")
gmail_key = os.environ.get("EMAIL_APP")
gmail_smtp = "smtp.gmail.com"


class NotificationManager:
    def __init__(self):
        self._client = Client(sms_api_id, sms_api_token)

    def send_message(self, body):
        message = self._client.messages \
            .create(
            body=body.strip(),
            from_='+12057549884',
            to='+821021157720'
        )
        return message.status

    def send_email(self, recipient, body, subject=None):
        if subject is None:
            subject = "We found a flight deal for you!"
        message = EmailMessage()
        message["From"] = my_gmail
        message["To"] = recipient
        message["Subject"] = subject
        message.set_content(body)

        with smtplib.SMTP(gmail_smtp, 587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.ehlo()
            connection.login(my_gmail, gmail_key)

            connection.send_message(msg=message)
