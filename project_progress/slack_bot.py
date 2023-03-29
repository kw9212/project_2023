import requests
import json

# This is the URL for the Slack webhook you want to use to send messages.
# You will need to create and use your own unique webhook URL.
# A Slack webhook URL is a unique address that allows you to send messages to a specific Slack channel or user.
# To learn how to create a webhook URL for your Slack workspace, please see the README.md file.
slack_webhook_url = "https://hooks.slack.com/services/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"

# We will be sending messages to our Slack channel in a way that utilizes webhooks.
def sendSlackWebhook(strText):
    headers = {
        "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        if res.status_code == 200:
            return "ok"
        else:
            return "error"

# If I receive this message via Slack, it will confirm that the program is functioning properly.
print(sendSlackWebhook("Hello, this is a message from python"))