<h1 align="center">EMAIL MARKETING BOT</h1>

![image](https://github.com/BhavdeepSinghNijhawan/Email-Marketing-Bot/assets/143419096/8109b397-e5ed-4d81-9a08-89208fa3be61)

- The Python script automates the process of sending marketing emails to a list of recipients. It utilizes the **smtplib library** for sending emails via an **SMTP server** and the **email.mime module** for constructing email messages.
- **Importing Required Libraries:** The script starts by importing necessary modules from the **smtplib** and **email.mime packages**. These are used for sending emails.
```
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
```
- **Print Welcome Message:** It prints a welcome message indicating the start of the email marketing process.
- **Email List:** The list emailList contains the email addresses to which the marketing emails will be sent. In a real-world scenario, this list might be populated from a **CSV file or a database**.
- **Defining the sendMail Function:** This function takes parameters for the sender's email address, recipient's email address, email subject, and email message. It then constructs an email message using MIMEMultipart and MIMEText objects. Finally, it sends the email via an **SMTP server using SSL encryption**.
- **Iterating Over Email List:** The script iterates over each email address in the emailList. For each email address, it sets the sender's email address, subject, and message, and then calls the sendMail function to send the email.
- **Sending Emails:** Inside the loop, emails are sent to each recipient sequentially. After sending each email, it prints a message indicating the email has been sent.
- **Delay Between Emails:** To avoid overloading the email server, the script pauses for **2 seconds** between sending each email.
- **Completion Message:** It prints a message indicating that all emails have been sent successfully.

## FEATURES

- Email List: The script supports reading recipient email addresses from a list. Currently, the email addresses are stored directly within the script for simplicity.
- Email Content: The email content, including the sender's email address, subject, and message body, is configurable within the script.
- SMTP Server: It connects to the SMTP server using SSL encryption (SMTP_SSL) provided by the smtplib library.
- Authentication: The script supports SMTP server authentication using environment variables for the sender's email address and password, enhancing security.
- Delay: It includes a time delay (2 seconds in this case) between sending each email to avoid overloading the SMTP server.
- Scalability: The code can be easily modified to handle a larger email list by reading email addresses from an external file or database.
- Security: The script uses SSL encryption for sending emails, ensuring that the communication with the SMTP server is secure.
- Customization: The email subject and message can be customized according to the requirements of the marketing campaign.
- Error Handling: Error handling for SMTP connection, login, and email sending is not included in this code snippet but would be essential in a production environment to handle potential issues gracefully.

## POTENTIAL IMPROVEMENTS

- Error Handling: Implement robust error handling to deal with potential exceptions during the email sending process.
- Configuration: Store sensitive information like email credentials securely, possibly using environment variables or a configuration file.
- Personalization: Add functionality to personalize emails with recipient names or other relevant information.

## USAGE

- Environment Setup: Before running the script, ensure that environment variables email and password are set to the sender's email address and password, respectively.
- Execution: Execute the script to start sending marketing emails to the recipients listed in the emailList variable.

## LANGUAGE

- Python

## TOOL

- Replit

## CONTRIBUTOR

- [Bhavdeep Singh Nijhawan](https://www.linkedin.com/in/bhavdeep-singh-nijhawan-739634280)
