# Examples

This document provides examples of how to use the functions in the Email Keyword Notifier project.

## Sending an email

```python
from email_sending import send_email

email_info = {
    "text": "This is a test email.",
    "Subject": "Test Email",
    "From": "sender@example.com",
    "To": "receiver@example.com",
    "send_email": "sender@example.com",
    "send_pwd": "password",
    "smtp_name": "smtp.example.com",
    "smtp_port": 587
}

send_email(email_info)
```
## Sending an email with attachment
```
from file_attachment import send_email_with_attachment

send_email = "sender@example.com"
send_pwd = "password"
smtp_name = "smtp.example.com"
smtp_port = 587
recv_email = "receiver@example.com"
subject = "Test Email with Attachment"
text = "This is a test email with an attachment."
file_path = "sample_file.txt"

send_email_with_attachment(send_email, send_pwd, smtp_name, smtp_port, recv_email, subject, text, file_path)
```
## Reading email titles
```python
import imaplib
from reading_email_title import read_email_titles

imap = imaplib.IMAP4_SSL("imap.example.com", 993)
imap.login("email@example.com", "password")

email_titles = read_email_titles(imap)
print(email_titles)

imap.logout()
```
## Reading email contents
```python
import imaplib
from reading_email_content import read_email_contents

imap = imaplib.IMAP4_SSL("imap.example.com", 993)
imap.login("email@example.com", "password")

email_contents = read_email_contents(imap)
print(email_contents)

imap.logout()
```

## Sending a Slack message using a webhook
```python
from slack_bot import sendSlackWebhook

message = "Hello, this is a test message for Slack."
webhook_url = "https://hooks.slack.com/services/your/webhook/url"

sendSlackWebhook(message, webhook_url)
```

## Sending notifications based on keywords
```python
import os
from send_notification import find_encoding_info

# You need to set the SLACK_WEBHOOK_URL environment variable to your Slack webhook URL.
os.environ["SLACK_WEBHOOK_URL"] = "https://hooks.slack.com/services/your/webhook/url"

# Example email data
emails = [
    {
        "From": "sender@example.com",
        "To": "receiver@example.com",
        "Date": "Mon, 4 Apr 2023 10:00:00 +0000",
        "Subject": "Thank you for your help!",
        "text": "Hello, I just wanted to say thank you for all your help.",
        "smtp_name": "smtp.example.com"
    }
]

for email_message in emails:
    email_from = email_message["From"]
    email_date = email_message["Date"]
    subject_str = email_message["Subject"]

    if subject_str.find("Thank you") >= 0:
        from slack_bot import sendSlackWebhook

        slack_send_message = email_from + "\n" + email_date + "\n" + subject_str
        webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "https://example.com/mock_url")
        sendSlackWebhook(slack_send_message, webhook_url)
        print(slack_send_message)
```

Please modify the examples with the appropriate email addresses, passwords, and file paths before using
