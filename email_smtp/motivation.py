import smtplib, os, datetime, random, sys
from email.message import EmailMessage

# exit the script if today's not Monday.
if datetime.datetime.now().weekday() != 6:
    sys.exit(0)

# Password and email (from environment variable)
gmail = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_APP")
receiver = "ikromov.suhrob@bk.ru"
gmail_server = "smtp.gmail.com"

msg = EmailMessage()
msg["Subject"] = "Monday motivation!"
msg["From"] = gmail
msg["To"] = gmail

with open("quotes.txt", "r+") as f:
    quotes = f.readlines()
    current_quote = random.choice(quotes)
    quote_of_week, author = current_quote.rsplit(" - ", maxsplit=1)
    msg.add_alternative(f"""
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Monday motivation</title>
    </head>
    <body>
        <p style="font-size: 20px;"><i>{quote_of_week}</i></p>
        <p style="font-size: 18px;"><b>{author}</b></p>
    </body>
    </html>
    """, subtype="html")


with smtplib.SMTP(gmail_server, 587) as connection:
    connection.ehlo()
    connection.starttls()
    connection.ehlo()

    connection.login(gmail, password)
    connection.send_message(msg)
