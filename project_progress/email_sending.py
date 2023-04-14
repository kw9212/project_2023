# Using Gmail's SMTP server, we send an email from python
# Author (KeunWoo Song, UNI: ks3651)

import smtplib
from email.mime.text import MIMEText


def send_email(email_info):
    msg = MIMEText(email_info["text"])

    msg["Subject"] = email_info["Subject"]
    msg["From"] = email_info["From"]
    msg["To"] = email_info["recv_email"]

    smtp_name = email_info["smtp_name"]
    smtp_port = email_info["smtp_port"]

    s = smtplib.SMTP(smtp_name, smtp_port)
    s.starttls()
    s.login(email_info["send_email"], email_info["send_pwd"])
    s.sendmail(email_info["send_email"], email_info["recv_email"], msg.as_string())
    s.quit()
