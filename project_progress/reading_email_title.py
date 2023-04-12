import subprocess
import time
import imaplib
import email
from email import policy

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

# Start the Greenmail server
greenmail_process = subprocess.Popen(["java", "-jar", "greenmail-standalone-2.1.0-alpha-1.jar", "-Dgreenmail.setup.test.imap"])
time.sleep(5)  # wait for the server to start up

# Login to Greenmail server
imap = imaplib.IMAP4("localhost", 3143)

# Read the first five emails from the inbox.
# You can adjust the number of emails to read by changing the number in [-5:]
imap.select("INBOX")
resp, data = imap.uid("search", None, "All")
all_email = data[0].split()
last_email = all_email[-5:]

for mail in reversed(last_email):
    result, data = imap.uid("fetch", mail, "(RFC822)")
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    print("=" * 70)
    print("FROM:", email_message["From"])
    print("SENDER:", email_message["Sender"])
    print("TO:", email_message["To"])
    print("DATE:", email_message["Date"])
    subject, encode = find_encoding_info(email_message["Subject"])
    print("SUBJECT:", subject)
    print("=" * 70)

imap.close()
imap.logout()

# Stop the Greenmail server
greenmail_process.kill()
