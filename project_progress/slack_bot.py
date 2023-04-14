import requests
import json


def sendSlackWebhook(strText, webhook_url):
    headers = {"Content-type": "application/json"}
    data = {"text": strText}

    res = requests.post(webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else:
        return "error"
