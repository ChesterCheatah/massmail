import smtplib
import csv
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import datetime
from email import encoders
import imaplib
from time import sleep
from random import randint

HOST = "smtp-mail.outlook.com"
MAILPORT = "587"
CREDENTIALS_USER =""
CREDENTIALS_PASS = ""
EMAIL_FROM_DEFAULT = ""
EMAIL_SUBJECT = "Ordernummer: "
EMAIL_CC_DEFAULT = ""
EMAIL_BCC_DEFAULT = ""


# Must be a csv file containing  
CONTACTS_FILE = r'contacts.csv'


# Set your Email Template here
def getEmailContent(first_name):

    curr_msg ="""
Hi """+first_name+""",
<br><br>
Email content goes here
<br><br>
Regards,<br>
"""+first_name+"""
    """

    return curr_msg

# Loops your contacts list (csv file)


    # Set up the SMTP server
def startsend(HOST, MAILPORT,CREDENTIALS_PASS, CREDENTIALS_USER, EMAIL_SUBJECT, curr_msg, email):
    try:
        print('Setting up connection to mail server')
        s = smtplib.SMTP(host=HOST, port=MAILPORT)
        s.starttls()
        s.login(CREDENTIALS_USER, CREDENTIALS_PASS)
        sleep(randint(1,3))
    except Exception as e:
        print(e); return "Error setting up the connection"
    print("Connection has been established")

    count = 1

    with open(filename, mode='r') as contacts_file:
        reader = csv.reader(contacts_file, delimiter=';')
        next(reader)
        for contact in reader:
            contact_full_name = contact[0]
            company = contact[1]
            title = contact[2]
            email = contact[3]
            first_name= contact[4]

            msg = MIMEMultipart()

            print(count)
            count = count +1
            print("Sending email to", contact_full_name)

            msg['From']=EMAIL_FROM_DEFAULT
            msg['To']=email
            msg['Bcc'] = EMAIL_BCC_DEFAULT
            msg['Subject']=  EMAIL_SUBJECT
            msg.attach(MIMEText(getEmailContent(first_name), 'html', "utf-8"))
            #print(type(msg))
            s.send_message(msg)
            del msg

            sleep(randint(10, 30))

            del msg

    s.quit()
    if error:
        return "Error occured while sending mails"
    else:
        return "Successful"
