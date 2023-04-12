import subprocess
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from nullsmtp import SMTP

# Start the Greenmail server
greenmail_process = subprocess.Popen(["java", "-jar", "greenmail-standalone-2.1.0-alpha-1.jar", "-Dgreenmail.setup.test.smtp"])
time.sleep(5)  # wait for the server to start up

# This is the email for testing.
send_email = "mytestemail@mailinator.com"
recv_email = "mytestemail@mailinator.com"

smtp_name = "localhost"
smtp_port = 3025

msg = MIMEMultipart()

msg["Subject"] = "This is a file attachment test"
msg["From"] = send_email
msg["To"] = recv_email

text = """
This is the sample email content.
"""

contentPart = MIMEText(text)
msg.attach(contentPart)

# Specify the path to the attachment
etc_file_path = r"project_2023/project_progress/sample_file.txt"

# reading the name of attaching file and attach it as a name of "filename"
with open(etc_file_path, "rb") as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header("Content-Disposition", "attachment", filename="sample_file.txt")
    msg.attach(etc_part)

# sending an email
s = SMTP(smtp_name, smtp_port)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

# Stop the Greenmail server
greenmail_process.kill()
