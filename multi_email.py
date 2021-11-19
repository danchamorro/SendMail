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

for email in list_of_emails:
    # loop through list of emails and send email to each one in list.
    sender = env.get("SENDER")
    recipient = email
    subject = "This is the subject"
    contents = """
    This is the contents of the email.
    """

    # Send the email using yagmail and the variables above as arguments to the function send with the contents of the email as the argument to the contents variable in the send function call below it.
    yag = yagmail.SMTP(sender, env.get("APP_PASSWORD"))
    yag.send(to=recipient, subject=subject, contents=contents)
print("Email sent!")
