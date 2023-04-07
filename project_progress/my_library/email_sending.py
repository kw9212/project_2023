# Using Gmail's SMTP server, we send an email from python
# Author (KeunWoo Song, UNI: ks3651)

# Using smtplib library
import smtplib
from email.mime.text import MIMEText

# Enter your naver ID here
# send_email = "userid@naver.com" (The sender has to be naver address for this project for now)
send_email = "kwsong9212@naver.com"

# To get the application password, please read README.md
send_pwd = "opensource!"

# Here we need the email address that you want to receive the message at.
recv_email = "ks3651@columbia.edu"

# smtp address for gmail
smtp_name = "smtp.naver.com"
smtp_port = 587

text = """
Write down contents of your mail here.
You can also enter multiple lines.
"""

msg = MIMEText(text)

# msg['Subject'] = "Enter the title of the email"
msg["Subject"] = "This is the sample"
msg["From"] = send_email
msg["To"] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()
