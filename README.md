<h1 align="center">InboxMaster</h1>

![image](https://github.com/BhavdeepSinghNijhawan/Email-Marketing-Bot/assets/143419096/8109b397-e5ed-4d81-9a08-89208fa3be61)

## FEATURES

- **Email List:** The script supports **reading recipient email addresses from a list**. Currently, the email addresses are stored directly within the script for simplicity.
- **Email Content:** The email content, including the sender's email address, subject, and message body, is configurable within the script.
- **SMTP Server:** It connects to the **SMTP server** using **`SSL encryption (SMTP_SSL) provided by the smtplib library`**.
- **Authentication:** The script supports **SMTP server authentication** using environment variables for the sender's email address and password, enhancing security.
- **Delay:** It includes a **time delay (2 seconds in this case)** between sending each email to **avoid overloading the SMTP server**.
- **Scalability:** The code can be easily modified to handle a larger email list by reading email addresses from an external file or database.
- **Security:** The script uses **SSL encryption** for sending emails, ensuring that the communication with the **SMTP server is secure**.
- **Customization:** The email subject and message can be customized according to the requirements of the marketing campaign.
- **Error Handling:** Error handling for SMTP connection, login, and email sending is not included in this code snippet but would be essential in a production environment to handle potential issues gracefully.

### SMTP

- SMTP stands for **Simple Mail Transfer Protocol**. It is a communication protocol used for transferring electronic mail (email) messages between servers. SMTP is a text-based protocol that operates over **TCP/IP networks**. SMTP is a reliable and efficient protocol for transferring email messages between mail servers. It operates on **port 25** by default, but encrypted variants like **SMTPS (SMTP Secure)** or SMTP over **TLS (Transport Layer Security**) are also commonly used to secure email transmission.

### SSL

- SSL stands for **"Secure Sockets Layer"**. It's a standard security protocol used to establish encrypted links between a web server and a browser in an online communication. SSL ensures that all data exchanged between the server and the browser remains **private** and **integral**. SSL encryption protects against eavesdropping and tampering by unauthorized parties. It's commonly used in securing online transactions, such as **e-commerce purchases**, **online banking**, and **sensitive data transfers**.

## POTENTIAL IMPROVEMENTS

- **Error Handling:** Implement **robust error handling** to deal with potential exceptions during the email sending process.
- **Configuration:** Store sensitive information like **email credentials** securely, possibly using environment variables or a configuration file.
- **Personalization:** Add functionality to personalize emails with recipient names or other relevant information.

## USAGE

- **Environment Setup:** Before running the script, ensure that environment variables email and password are set to the sender's email address and password, respectively.
- **Execution:** Execute the script to start sending marketing emails to the recipients listed in the emailList variable.

## LANGUAGE

- Python

- **Importing Required Libraries:** The script starts by importing necessary modules from the **`smtplib`** and **`email.mime packages`**. These are used for sending emails.

```
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
```

- **Print Welcome Message:** It prints a welcome message indicating the start of the email marketing process.

```
print("Welcome to InboxMaster")
```

- **Email List:** The list emailList contains the email addresses to which the marketing emails will be sent. In a real-world scenario, this list might be populated from a **CSV file or a database**.

```
emailList = ['########', '########', '########']
```

- **Defining the sendMail Function:** This function takes parameters for the sender's email address, recipient's email address, email subject, and email message. It then constructs an email message using **`MIMEMultipart`** and MIMEText objects. Finally, it sends the email via an **SMTP server using SSL encryption**.

```
def sendMail(fromEmail, toEmail, subject, message):
```

- This line defines a function named **`sendMail`** that takes four parameters: **`fromEmail (sender's email address)`**, **`toEmail (recipient's email address)`**, **`subject (email subject)`**, and **`message (email body)`**.

```
  msg = MIMEMultipart()
  msg.set_unixfrom("BhavdeepSinghNijhawan")
  msg['From'] = fromEmail
  msg['To'] = toEmail
  msg['Subject'] = subject
  msg.attach(MIMEText(message))
```

- These lines create a new **`MIMEMultipart`** message object and set its attributes such as sender, recipient, subject, and message body.

```
  mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
  mailserver.ehlo()
  mailserver.login(os.environ['email'], os.environ['password'])
```

- These lines create an **SMTP server** object using **SSL encryption** and connect to the SMTP server. The login method is then used to authenticate the user using the email and password obtained from environment variables.

```
  mailserver.sendmail(fromEmail, toEmail, msg.as_string())
  mailserver.quit()
```

- **Iterating Over Email List:** The script iterates over each email address in the emailList. For each email address, it sets the sender's email address, subject, and message, and then calls the **`sendMail`** function to send the email.

```
for email in emailList: 
  fromEmail = "########"
  subject = "Welcome to InboxMaster"
  message = "This is a Test for InboxMaster"
  sendMail(fromEmail, email, subject, message)
```

- **Sending Emails:** Inside the loop, emails are sent to each recipient sequentially. After sending each email, it prints a message indicating the email has been sent.

```
print(f"Mail sent to - {email}")
```

- **Delay Between Emails:** To avoid overloading the email server, the script pauses for **2 seconds** between sending each email.

```
time.sleep(2)
```

- **Completion Message:** It prints a message indicating that all emails have been sent successfully.

```
print("All E-Mails are Sent Successfully")
```

## TOOL

- [Replit](https://replit.com/)

## CONTRIBUTOR

- [Bhavdeep Singh Nijhawan](https://www.linkedin.com/in/bhavdeep-singh-nijhawan-739634280)
