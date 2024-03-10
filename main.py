##################### Normal Starting Project ######################
import smtplib
import datetime
import pandas as pd
import datetime as dt
import random

now=dt.datetime.now()
today_tuple = (now.month, now.day, now.year, now.hour, now.minute, now.second)
data = pd.read_csv('birthdays.csv')

birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(0,3)}.txt"

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



