import datetime


class FlightData:
    def __init__(self, data):
        self.currency = data.get("currency")
        self.price = int(data["data"][0].get("price"))
        self.fly_from = data["data"][0].get("cityFrom")
        self.fly_from_code = data["data"][0].get("flyFrom")

        self.fly_to = data["data"][0].get("cityTo")
        self.fly_to_code = data["data"][0].get("flyTo")
        duration_seconds = data["data"][0].get("duration").get("departure")
        self.duration = str(duration_seconds // 3600) + ":" + str(duration_seconds//60 % 60)

        departure_str = data["data"][0].get("route")[0].get("local_departure")
        arrival_str = data["data"][0].get("route")[0].get("local_arrival")
        self.departure = datetime.datetime.strptime(departure_str, "%Y-%m-%dT%H:%M:%S.000Z")
        self.arrival = datetime.datetime.strptime(arrival_str, "%Y-%m-%dT%H:%M:%S.000Z")

        self.booking_link = data["data"][0].get("deep_link")

