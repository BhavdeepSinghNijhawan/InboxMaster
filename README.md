# Email Marketing Bot

This Python script automates the process of sending marketing emails to a list of recipients. It utilizes the smtplib library for sending emails via an SMTP server and the email.mime module for constructing email messages.

![image](https://github.com/BhavdeepSinghNijhawan/Email-Marketing-Bot/assets/143419096/8109b397-e5ed-4d81-9a08-89208fa3be61)

# Language Used

- Python

# Features

- Email List: The script supports reading recipient email addresses from a list. Currently, the email addresses are stored directly within the script for simplicity.
- Email Content: The email content, including the sender's email address, subject, and message body, is configurable within the script.
- SMTP Server: It connects to the SMTP server using SSL encryption (SMTP_SSL) provided by the smtplib library.
- Authentication: The script supports SMTP server authentication using environment variables for the sender's email address and password, enhancing security.
- Delay: It includes a time delay (2 seconds in this case) between sending each email to avoid overloading the SMTP server.

# Usage

- Environment Setup: Before running the script, ensure that environment variables email and password are set to the sender's email address and password, respectively.
- Execution: Execute the script to start sending marketing emails to the recipients listed in the emailList variable.

# Contributor

- [Bhavdeep Singh Nijhawan](https://www.linkedin.com/in/bhavdeep-singh-nijhawan-739634280)
