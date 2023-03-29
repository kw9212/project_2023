import requests
import json

# This is my url. You need to create and use your own url.
# To get a slack_webhook_url, please see the readMe.md.
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