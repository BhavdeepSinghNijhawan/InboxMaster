#Author: Bhavdeep Singh Nijhawan

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time

print("Welcome to InboxMaster")
# This can be Read from a .csv file
emailList = ['########', '########', '########']

def sendMail(fromEmail, toEmail, subject, message):
  msg = MIMEMultipart()
  msg.set_unixfrom("BhavdeepSinghNijhawan")
  msg['From'] = fromEmail
  msg['To'] = toEmail
  msg['Subject'] = subject
  msg.attach(MIMEText(message))
  mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
  mailserver.ehlo()
  mailserver.login(os.environ['email'], os.environ['password']) 
  
  mailserver.sendmail(fromEmail, toEmail, msg.as_string())
  mailserver.quit()
  
for email in emailList: 
  fromEmail = "########"
  subject = "Welcome to InboxMaster"
  message = "This is a Test for InboxMaster"
  sendMail(fromEmail, email, subject, message)
  print(f"Mail sent to - {email}")
  time.sleep(2)

print("All E-Mails are Sent Successfully")
