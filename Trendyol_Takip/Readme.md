# Trendyol Price Tracker

This Python script allows you to track the price of a product on Trendyol and receive email notifications when the price drops below a specified threshold.

## Prerequisites

Before using the Trendyol Price Tracker, ensure you have the following prerequisites installed:

- Python 3.x
- Required Python libraries (`requests`, `bs4`, and `smtplib`)

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4

# Getting Started
1. Modify the send_email.py file:

Replace "KIME_EMAIL", "KIMDEN_EMAIL", and "EMAIL_SIFRE" with your email address and credentials.

2.Run the script:
python your_script_name.py

#Configuration
url1: The URL of the product on Trendyol that you want to track.
paramPrice: Your desired price threshold. You will receive an email notification when the price drops below this threshold.

#Usage
The script will continuously check the price of the product and send an email notification if the price falls below the specified threshold.
