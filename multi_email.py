import os
import yagmail
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

df = pd.read_csv('emails.csv')

# add emails to list
list_of_emails = df["email"].to_list()

# Put the os.environ in a variable
env = os.environ

# Login to email once
sender = env.get("SENDER")
yag = yagmail.SMTP(sender, env.get("APP_PASSWORD"))

for email in list_of_emails:
    # loop through list of emails and send email to each one in list.
    recipient = email
    subject = "This is the subject"
    contents = """
    This is the contents of the email.
    """
    # Send the email using yagmail
    yag.send(to=recipient, subject=subject, contents=contents)
print("Email sent!")
