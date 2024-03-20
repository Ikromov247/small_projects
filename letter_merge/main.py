from datetime import date
import os

os.mkdir("Output")
recipients = ["Dave Batista", "Miguel Servantes",
              "Sandra Bullock", "Mitchell Pritchett", "Lana Del Rey", "Ethan Hawke"]

with open("letter.txt", "r") as template:
    for recipient in recipients:
        name = recipient.split()[0].lower()
        with open(f"Output/letter_to_{name}.txt", "w") as letter:
            letter.write(f"{date.today()}\n\n")
            letter.write(f"Dear {name.capitalize()},\n\n")
            letter.write(template.read())
            template.seek(0)
        print(template.readline())
