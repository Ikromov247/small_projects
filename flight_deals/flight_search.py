import datetime
import requests


class FlightSearch:
    def __init__(self, base_city="Seoul"):
        tday = datetime.date.today()
        self._date_from = (tday + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        self._date_to = (tday + datetime.timedelta(days=180)).strftime("%d/%m/%Y")
        self._api = ""
        self._endpoint = "https://tequila-api.kiwi.com/"  # +/v2 if searching for flights
        self._header = {
            "apikey": self._api
        }
        self._base_city = base_city
        self._base_city_iata = self.get_city_code(base_city)

    def get_city_code(self, city: str) -> str:
        query = "locations/query"
        iata_params = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": "5",
            "sort": "name"
        }
        response = requests.get(url=self._endpoint + query, params=iata_params, headers=self._header).json()
        # iterate the results
        for location in response["locations"]:
            # and find/return matching city's iata code
            if location.get("city").get("name") == city:
                iata_code = location.get("city").get("code")

                return iata_code
        if city not in [data["city"]["name"] for data in response["locations"]]:
            return "none"  # not found

    def get_flight_deal(self,
                        city,
                        adults: int = 1,
                        max_fly_duration: int = 30,
                        luggage: int = 1
                        ) -> dict:
        """:returns application/json as dict
            takes city IATA codes as input
        """
        # if cities_iata is not None:
        #     fly_to = ",".join(cities_iata)
        fly_from = self._base_city_iata

        fly_to = city
        if type(city) is list:
            fly_to = ",".join(city)

        query = "v2/search"
        flight_params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": self._date_from,
            "date_to": self._date_to,
            # "nights_in_dst_from": 1,
            # "nights_in_dst_to": 3,
            "max_fly_duration": max_fly_duration,
            "flight_type": "oneway",
            "one_for_city": 1,
            "adults": adults,
            "selected_cabins": "M",
            "adult_hold_bag": luggage,
            "adult_hand_bag": 1,
            "locale": "en",
            "curr": "USD"
        }
        flights = requests.get(url=self._endpoint + query, params=flight_params, headers=self._header).json()
        return flights
