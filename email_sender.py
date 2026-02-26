from email.message import EmailMessage
import os
from dotenv import load_dotenv
import ssl
import smtplib

load_dotenv()

email_sender = "etikonapal@gmail.com"
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = "mexati5831@netoiu.com"

subject = "Top 7 Startup Stories This Week- 7-Minutes to Read"

body = """
In last 7 days,
Top 7 News
Read in 7 minutes.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)