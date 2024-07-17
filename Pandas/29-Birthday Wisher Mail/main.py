import datetime as dt
import smtplib
import pandas as pd
from random import randint

my_email = "example@gmail.com"
password = "password"

now = dt.datetime.now()
today_month = now.month
today_day = now.day


data = pd.read_csv("Pandas/29-Birthday Wisher Mail/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if (today_month, today_day) in birthdays_dict:
    file_name = f"Pandas/29-Birthday Wisher Mail/letter_templates/letter_{randint(1,3)}.txt"
    with open(file_name) as data:
        content = data.read()
    
    name = birthdays_dict[(today_month, today_day)]["name"]
    personalized_letter = content.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)          
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dict[(today_month, today_day)]["email"],
            msg=f"Subject:Happy Birthday\n\n{personalized_letter}"
        )
