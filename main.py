import pandas as pd
import datetime as dt
from random import randint, choice
import smtplib

MY_EMAIL = "EMAIL@GMAIL.COM"
MY_PASSWORD = "123456789DEZ"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    pd.read_excel(".xlsx")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_PASSWORD,
                            msg="Subject: XXXX\n\n"
                                "Message")



