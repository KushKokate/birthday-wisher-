import smtplib
import datetime
import pandas as pd
import random

email = "kokatekush96@gmail.com"
password = "fpat knvr rohz cgzg"

# Get current date
now = datetime.datetime.now()
today_tuple = (now.month, now.day)

# Read CSV file
data = pd.read_csv('birthdays.csv')

# Create a dictionary of birthdays from the CSV data
birthdays_dict = {(row["month"], row["day"]): row for index, row in data.iterrows()}

# Check if today's date matches any birthday in the dictionary
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # Select a random letter template
    file_path = f"letter_templates/letter_{random.randint(0, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email, password)
        server.sendmail(from_addr=email,
                        to_addrs=birthday_person["email"],
                        msg=f"Subject: Happy Birthday\n\n{contents}")
