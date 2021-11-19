import os
import yagmail
from dotenv import load_dotenv

load_dotenv()

# Put the os.environ in a variable
env = os.environ

# Get the email address from the .env file and put it in a variable
sender = env.get("SENDER")
recipient = env.get("RECIPIENT")
subject = "This is the subject"
contents = """
This is the contents of the email.
"""

# Send the email using yagmail and the variables above as arguments to the function send with the contents of the email as the argument to the contents variable in the send function call below it.
yag = yagmail.SMTP(sender, env.get("APP_PASSWORD"))
yag.send(to=recipient, subject=subject, contents=contents)
print("Email sent!")
