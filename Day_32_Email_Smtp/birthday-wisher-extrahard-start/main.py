##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import smtplib
import datetime as dt

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
year = today.year
month = today.month
day = today.day
date_df = pd.read_csv("Day_32_Email_Smtp/birthday-wisher-extrahard-start/birthdays.csv")
matching_dates = date_df[(date_df['year'] == year) & (date_df['month'] == month) & (date_df['day'] == day)]

if len(matching_dates) > 0 :
    bd_name = matching_dates['name'].to_list()[0]
    bd_email = matching_dates['email'].to_list()[0]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    list = [1,2,3]
    list_val = random.choice(list)
    with open(f'Day_32_Email_Smtp/birthday-wisher-extrahard-start/letter_templates/letter_{list_val}.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.replace('[NAME]', bd_name)

# 4. Send the letter generated in step 3 to that person's email address.

    email = '########@gmail.com'
    password = '#########'

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr='',to_addrs=bd_email ,msg=f'Subject:HOB\n\n{content}')





