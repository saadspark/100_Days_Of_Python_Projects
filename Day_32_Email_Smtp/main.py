import smtplib
import datetime as dt
import random


file_path = "Day_32_Email_Smtp/quotes.txt"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()


random_quote = random.choice(lines)


date = dt.datetime(year=2024, month=7, day=28).date()
today = dt.datetime.now().date()
if date == today:
    email = '@gmail.com'
    password = ''
    # Connect to the SMTP server
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=email, password=password)
    
    # Send the email
    connection.sendmail(
        from_addr=email,
        to_addrs="saadahmadspark@gmail.com",
        msg=f"Subject: Motivation Quote of the Day\n{random_quote}"
    )
    print("Email sent successfully")
    
    # Close the SMTP connection
    connection.quit()