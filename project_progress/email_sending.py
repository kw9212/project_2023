import subprocess
import time
from email.mime.text import MIMEText
from nullsmtp import SMTP

# Start the Greenmail server
greenmail_process = subprocess.Popen(["java", "-jar", "greenmail-standalone-2.1.0-alpha-1.jar", "-Dgreenmail.setup.test.smtp"])
time.sleep(5)  # wait for the server to start up

# This is the email for testing.
send_email = "mytestemail@mailinator.com"
recv_email = "mytestemail@mailinator.com"

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

s = SMTP("localhost", 3025)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

# Stop the Greenmail server
greenmail_process.kill()
