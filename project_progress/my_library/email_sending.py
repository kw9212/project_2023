# Using Gmail's SMTP server, we send an email from python
# Author (KeunWoo Song, UNI: ks3651)

# Using smtplib library
import smtplib
from email.mime.text import MIMEText

# Enter your gmail ID here
# send_email = "GmailID@gmail.com" (The sender has to be gmail address for this project for now)
send_email = " "

# To get the application password, please read README.md
# send_pwd = "Google Application password"
send_pwd = " "

# Here we need the email address that you want to receive the message at.
recv_email = " "

# smtp address for gmail
smtp_name = "smtp.gmail.com"
smtp_port = 587

text = """
Write down contents of your mail here.
You can also enter multiple lines.
"""

msg = MIMEText(text)

# msg['Subject'] = "Enter the title of the email"
msg['Subject'] = "This is the sample"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()
