import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Enter your gmail ID here and application password
# To get the application password, please read README.md
send_email = "Google account@gmial.com"
send_pwd = "Google PW"

# ex) recv_email = "ks3651@columbia.edu" (The sender has to be gmail address for this project for now)
recv_email = "Email address"

smtp_name = "smtp.gmail.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = "This is a file attachment test"
msg['From'] = send_email
msg['To'] = recv_email

text = """
This is the sample email contect.
"""

contentPart = MIMEText(text)
msg.attach(contentPart)

# Specify the path to the attachment
etc_file_path = r'project_2023./project_progress/sample_file.txt'

# reading the name of attaching file and attach it as a name of "filename"
with open(etc_file_path, 'rb') as f :
    etc_part = MIMEApplication( f.read() )
    etc_part.add_header('Content-Disposition','attachment', filename = "sample_file.txt")
    msg.attach(etc_part)

# sending an email
s = smtplib.SMTP( smtp_name, smtp_port)
s.starttls()
s.login( send_email , send_pwd)
s.sendmail( send_email, recv_email, msg.as_string())
s.quit()
