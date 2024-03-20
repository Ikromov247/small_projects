import pandas as pd
import random
import json


class password_mngr:
    lower_letters = [chr(order) for order in range(ord("a"), ord("z") + 1)]
    upper_letters = [chr(order) for order in range(ord("A"), ord("Z") + 1)]
    digits = [str(num) for num in range(0, 10)]
    characters = [chr(order) for order in range(33, 48) if chr(order) not in ["'", '"']]

    def __init__(self):
        self.website = ""
        self.username = ""
        self.password = ""

    @staticmethod
    def generate_password(cls):
        """returns a random password
            with 4 lowercase, 4 uppercase letters,
            2 characters, 2 digits
        """
        password = ""
        letters = random.choices(cls.lower_letters, k=4)
        up_letters = random.choices(cls.upper_letters, k=4)
        characters = random.choices(cls.characters, k=2)
        digits = random.choices(cls.digits, k=2)
        components = [letters, up_letters, characters, digits]
        # join components in a random order
        for _ in range(4):
            current_component = random.choice(components)
            password += "".join(current_component)
            components.remove(current_component)
        return password

    @staticmethod
    def add_password(website, username, password):
        if website != "" and username != "" and password != "":
            new_data = {
                f"{website}": {
                    "username": username,
                    "password": password
                }
            }
            try:
                # update the opened json with new password details
                with open("password_database.json", "r") as file:
                    database = json.load(file)

            except FileNotFoundError:
                # if file doesn't exist, create it and add new data
                with open("password_database.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                database.update(new_data)
                # save the updated data to the original file
                # if file exists
                with open("password_database.json", "w") as file:
                    json.dump(database, file, indent=4)
                # added successfully
            finally:
                return "0"
        else:
            # one or more of the entries is missing
            return "404"

    @staticmethod
    def find_password(website):
        """returns password for the first found match.\n
            Requires either website name as example.com,\n
            or username as John Doe, case-sensitive.
        """
        file = open("password_database.json", "r")
        database = json.load(file)
        try:
            website_data = database[f"{website}"]
            username = website_data["username"]
            password = website_data["password"]
            return username, password
        except:
            return "not found", ""
        finally:
            file.close()


