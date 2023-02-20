# Here we send an email with Python code and read the email address recorded in the excel file 
# to automatically sends a large amount of email (Gmail)

import smtplib
from email.mime.text import MIMEText

# Enter your gmail ID here
send_email = "GmailID@gmail.com"

# Enter the 16-digit password generated through the app password
send_pwd = "Google Application password"

recv_email = "recipient email address@gmail.com"

# smtp address for gmail
smtp_name = "stmp.gmail.com"
smtp_port = 587

text = """
Write down contents of your mail here.
You can also enter multiple lines.
"""

msg = MIMEText(Text)

msg['Subject'] = "Enter the title of the email"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP( smtp_name , smtp_port)
s.starttls()
s.login( send_email, send_pwd)
s.sendmail( send_email, recv_email, msg.as_string())
s.quit()
