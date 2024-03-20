import os, smtplib
from email.message import EmailMessage
import imghdr

gmail = os.environ.get("EMAIL")
password = ""
receiver = ""
gmail_server = "smtp.gmail.com"

msg = EmailMessage()
msg["Subject"] = "Test"
msg["From"] = gmail
msg["To"] = receiver

msg.set_content("Hello, old timer.\n-------\nfrom Sukhrob")
msg.add_alternative("""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test</title>
</head>
<body>
    <h1 style="color:SlateGray;">Hello old timer</h1>
</body>
</html>
""", subtype="html")
# path = r"D:\Downloads\100-days-of-code\32 Day 32 - Intermediate+ Send Email (smtplib) & Manage Dates (datetime)\286 Day 32 Goals_ what we will make by the end of the day.mp4"
# with open(path, "rb") as img_file:
#     data = img_file.read()
#     name = img_file.name
#
#     msg.add_attachment(data, filename=name, maintype="video", subtype="MPEG-4")

with smtplib.SMTP_SSL(gmail_server, 465) as connection:
    # connection.ehlo()
    # connection.starttls()
    # connection.ehlo()
    connection.login(gmail, password)
    connection.send_message(msg)
