# Sending Notifications to Your Smartphone for Specific Keywords in Emails
The project involves creating a program that reads gmail and sends notifications to your smartphone using slack when a specific keyword appears.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Issue](https://img.shields.io/github/issues/kw9212/project_2023)](https://github.com/kw9212/project_2023.git)
![](https://github.com/kw9212/project_2023/actions/workflows/build.yml/badge.svg)
[![codecov](https://codecov.io/github/kw9212/project_2023/branch/main/graph/badge.svg?token=05c337ef-226f-41c3-b136-0fe9842b5192)](https://codecov.io/github/kw9212/project_2023)

## Overview
This idea came from the challenge of having to sort through many emails every day to find the important ones. Gmail already has a labeling function that classifies emails based on specific email addresses as filters. This project aims to create a function that sends notifications based on keywords using slack and smartphones. There is also potential to expand this project to find information in other ways besides just keywords.

### How to generate an application-specific password in Gmail
In order to use Gmail's SMTP server to send emails from Python, you need to generate an application-specific password instead of using your account password.

Here are the steps to generate an application-specific password in Gmail:

1. Go to your Google account settings by visiting https://myaccount.google.com/.
2. Click on "Security" in the left-hand menu.
3. Scroll down to the "Signing in to Google" section and click on "App passwords".
4. If prompted, sign in to your Google account again.
5. Select "Mail" from the list of applications and "Other (custom name)" from the list of devices.
6. Type in a name for the application-specific password, such as "Python email script", and click "Generate".
7. Google will generate a 16-character password that you can use in your Python script to authenticate with Gmail's SMTP server.
Once you have generated the application-specific password, you can use it in your Python script to authenticate with Gmail's SMTP server and send emails.

### slack_bot.py
In order to get a Slack webhook URL:

1. Go to the Slack API website and sign in to your workspace.
2. Click on the "Create New App" button and give your app a name.
3. Once your app is created, navigate to the "Incoming Webhooks" section and toggle the switch to "On".
4. Click on "Add New Webhook to Workspace" and select the channel where you want to receive messages from your Python script.
5. Click on "Authorize" to allow your app to access your Slack workspace.
6. Once the webhook is created, you will see a "Webhook URL" field. Copy the URL to your clipboard.
7. Use this URL as your slack_webhook_url in your Python script. 

That's it! You can now use this webhook URL in your Python script to send messages to your Slack channel.
