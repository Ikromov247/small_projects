import pytz
import os
import requests
import datetime

exercise_apisid = ""
exercise_apikey = ""
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercises_done = []

exercise_header = {
    "x-app-id": exercise_apisid,
    "x-app-key": exercise_apikey,
    "Content-Type": "application/json"
}
exercise_params = {
    "query": input("What did you do today? ").strip(),
    "gender": "male",
    "weight_kg": 57.0,
    "height_cm": 178.5,
    "age": 20
}
exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_header).json()

tday_datetime = datetime.datetime.now(tz=pytz.timezone("Asia/Seoul"))
tday_date = tday_datetime.strftime("%d/%m/%Y")
tday_time = tday_datetime.strftime("%H:%M:%S")

for exercise in exercise_response["exercises"]:
    # print(exercise)
    exercises_done.append({"date": tday_date,
                           "time": tday_time,
                           "exercise": exercise.get("name").capitalize(),
                           "duration": exercise.get("duration_min"),
                           "calories": exercise.get("nf_calories")
                           })

sheety_auth = "Bearer yawmttwdbGGFSF1924"
sheety_username = "sukhrob"
sheety_password = "ikramov1"
sheety_endpoint = "https://api.sheety.co/ddd7ed3308d095087fe2297eb3689f95/myWorkouts/workouts"

for exercise_done in exercises_done:
    print(exercise_done)
    sheety_response = requests.post(
        url=sheety_endpoint,
        json={"workout": exercise_done},
        headers={"Authorization": sheety_auth}
    )

    print(sheety_response.text)
