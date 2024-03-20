import requests
from flight_search import FlightSearch


class DataManager:
    def __init__(self):
        self.flight_search = FlightSearch()
        self._auth = ""
        self.header = {
            "Authorization": self._auth
        }
        self._sid = ""
        self._endpoint = f"https://api.sheety.co/{self._sid}/flightDeals/"
        self.cities = self._get_data()

    def _get_data(self):
        query = "flights"
        cities = []

        response = requests.get(url=self._endpoint + "/" + query, headers=self.header).json()["flights"]

        for city in response:

            if len(city["iataCode"]) > 2:
                cities.append(
                    {"city": city["city"],
                     "iataCode": city["iataCode"],
                     "lowestPrice": city["lowestPrice"]})
            else:
                city_code = self.flight_search.get_city_code(city["city"])
                data = {
                    "iataCode": city_code,
                }
                cities.append(
                    {"city": city["city"],
                     "iataCode": city_code,
                     "lowestPrice": city["lowestPrice"]})

                response = requests.put(
                    url=self._endpoint + "/" + query + "/" + str(city["id"]),
                    json={"flights": data},
                    headers=self.header)

        return cities

    def add_users(self, user: dict):
        query = "users"
        first_name = user["first_name"]
        last_name = user["last_name"]
        e_mail = user["email"]
        data = {
            "firstName": first_name,
            "lastName": last_name,
            "email": e_mail
        }
        response = requests.post(url=self._endpoint + "/" + query, json={"user": data}, headers=self.header)
        return response.text

    def get_users(self):
        query = "users"
        response = requests.get(url=self._endpoint + "/" + query, headers=self.header).json()["users"]
        return response
