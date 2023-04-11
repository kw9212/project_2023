import imaplib
import email
from email import policy
import requests
import json

# This is the URL for the Slack webhook you want to use to send messages.
# You will need to create and use your own unique webhook URL.
# A Slack webhook URL is a unique address that allows you to send messages to a specific Slack channel or user.
# To learn how to create a webhook URL for your Slack workspace, please see the README.md file.
slack_webhook_url = "https://hooks.slack.com/services/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"


def sendSlackWebhook(strText):
    headers = {"Content-type": "application/json"}

    data = {"text": strText}

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else:
        return "error"


def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode


imap = imaplib.IMAP4_SSL("imap.naver.com")

# Use the application password for authentication
# To obtain an application password, please refer to README.md
id = "kwsong9212"
pw = "opensource!"
imap.login(id, pw)

imap.select("INBOX")
resp, data = imap.uid("search", None, "All")
all_email = data[0].split()
last_email = all_email[-5:]

for mail in reversed(last_email):
    result, data = imap.uid("fetch", mail, "(RFC822)")
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    email_from = str(email_message["From"])
    email_date = str(email_message["Date"])
    subject, encode = find_encoding_info(email_message["Subject"])
    subject_str = str(subject)

    # Enter the keyword you want to filter out of the email.
    # If the program finds the keyword, it returns the location. Otherwise, it returns -1.
    # In this case, the program will find the email that contains "Key" in the content.
    # You can customize the word you want to find in your email.
    if subject_str.find("Thank you") >= 0:
        slack_send_message = email_from + "\n" + email_date + "\n" + subject_str
        sendSlackWebhook(slack_send_message)
        print(slack_send_message)

imap.close()
imap.logout()
