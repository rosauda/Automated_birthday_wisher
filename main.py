import pandas as pd
import datetime as dt
import random
import smtplib
from random import choice, randint

MY_EMAIL = "example@XXXXX.com"  # your email
MY_PASSWORD = "XXXXXXXXXXX"  # app password of your account

# ---------------------------- DISCOVERING WHO IS CELEBRATING BIRTHDAY TODAY ------------------------------- #

# Reading csv file, creating string month + day
data = pd.read_csv("birthdays.csv")
data["MONTH_DAY"] = data['month'].astype(str) + data['day'].astype(str)

# Date now, creating string month + day
now = dt.datetime.now()
day = now.day
month = now.month
check_date = str(month) + str(day)

# Checking number of people celebrating birthday today
found = (check_date in data['MONTH_DAY'].unique())
information_birthday = data.loc[data["MONTH_DAY"] == check_date]
number_people = information_birthday["email"].count()

try:
    for i in range(0, number_people):
        # If true, retrieve information
        if found:
            information = data.loc[data["MONTH_DAY"] == check_date]
            information_name = information["name"].iloc[i]
            information_email = information["email"].iloc[i]

            # ---------------------------- CHOOSING AND EDITING RANDOM LETTER ------------------------------- #

            letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
            random_letter = random.choice(letters_list)

            # Editing selected letter with correct information
            with open(str(random_letter)) as letter:
                letter_edited = letter
                letter_edited = letter_edited.read()
                letter_edited = letter_edited.replace('[NAME]', f'{information_name}')
                letter.close()

            # ---------------------------- SENDING EMAIL ------------------------------- #

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=information_email,
                                    msg=f"Subject: Happy birthday {information_name}\n\n"
                                        f"{letter_edited}")
        else:
            pass

except smtplib.SMTPAuthenticationError:
    pass
