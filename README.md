# Sending Notifications to Your Smartphone for Specific Keywords in Emails
The project involves creating a program that reads gmail and sends notifications to your smartphone using slack when a specific keyword appears.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![](https://img.shields.io/github/issues/kw9212/project_2023)
[![Build Status](https://github.com/kw9212/project_2023/workflows/Build%20Status/badge.svg?branch=main&cachebuster=1)](https://github.com/kw9212/project_2023/actions)
![](https://github.com/kw9212/project_2023/actions/workflows/build.yml/badge.svg)
[![codecov](https://codecov.io/github/kw9212/project_2023/branch/main/graph/badge.svg?token=05c337ef-226f-41c3-b136-0fe9842b5192)](https://app.codecov.io/gh/kw9212/project_2023)
[![PyPI](https://img.shields.io/pypi/v/project-2023)](https://pypi.org/project/project-2023/)
[![Documentation Status](https://readthedocs.org/projects/project-2023/badge/?version=latest)](https://project-2023.readthedocs.io/en/latest/?badge=latest)


Overview
--------

This idea came from the challenge of having to sort through many emails every day to find the important ones. Gmail already has a labeling function that classifies emails based on specific email addresses as filters. This project aims to create a function that sends notifications based on keywords using slack and smartphones. There is also potential to expand this project to find information in other ways besides just keywords.

Installing
----------

.. code-block:: bash

    pip install project_progress

Dependencies
------------

- slack_sdk

Usage
-----

.. code-block:: python

    from project_progress import read_email_titles, sendSlackWebhook

    email_titles = read_email_titles()
    keyword = "important"

    for title in email_titles:
        if keyword in title:
            sendSlackWebhook("Keyword found in email title: " + title, webhook_url)


For more detailed usage instructions and available options, please refer to the [documentation](./documentation.md).
