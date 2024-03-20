import datetime
import pytz

dt_now = datetime.datetime.now(tz=pytz.timezone("Asia/Seoul"))
print(dt_now.strftime("%B %d, %Y"))
str_date = "August 21, 2022"
dt = datetime.datetime.strptime(str_date, "%B %d, %Y")
print(dt)
