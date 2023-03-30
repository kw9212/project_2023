import imaplib
import email
from email import policy

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

# Login to Gmail account
imap = imaplib.IMAP4_SSL('imap.gmail.com')

# Use the application password for authentication
# To obtain an application password, please refer to README.md
id = 'Google Email address'
pw = 'application password'
imap.login(id, pw)

imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-5:]

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    print('='*70)
    print('FROM:', email_message['FROM'])
    print('SENDER:', email_message['SENDER'])
    print('TO:', email_message['To'])
    print('DATE:', email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    print('SUBJECT:', subject)

# Read the content of the email and print it. Only save the content if the message type is text/plain.
# Program does not read attachments, only text/plain emails are saved.
    print('[CONTENT]')
    message = ''
    if email_message.is_multipart():
        for part in email_message.get_payload():
            if part.get_content_type() == 'text/plain':
                bytes = part.get_payload(decode=True)
                encode = part.get_content_charset()
                message = message + str(bytes, encode)

    print(message)
    # Separate each email with a line of '=' characters.
    print('='*70)

imap.close()
imap.logout()