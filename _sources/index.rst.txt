.. EmailKeywordNotifier documentation master file, created by
   sphinx-quickstart on Mon Apr 24 00:43:10 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Email Keyword Notifier's documentation!
==================================================

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

For more detailed usage instructions and available options, please refer to the 'Examples' section, either below or in the left navigation menu.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   project_progress
   examples.md

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`