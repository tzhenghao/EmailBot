# Name: Zheng Hao Tan
# Email: tanzhao@umich.edu
# Date: May 16, 2015

# This program is to be used in conjunction with my Task Scheduler Bot that runs
# as a daemon for handling other tasks, including my emails.

# USAGE: python3 emailBot.py <OUTLOOK, UMICH, GMAIL>

import os, re, logging, sys
import smtplib

import email_setup

# EFFECTS: Sends a reply based on the email address, subject and content provided.
def sendReply(emailAddress, recipient, subject, content):
	if emailAddress == 'GMAIL':
		sendReplyGmail(recipient, subject, content)
	elif emailAddress == 'OUTLOOK':
		sendReplyOutlook(recipient, subject, content)
	elif emailAddress == 'UMICH':
		sendReplyUMich(recipient, subject, content)

# REQUIRES: The smtp server domain name, port number, username and password.
# EFFECTS: Logs in to the SMTP server and returns the SMTP object.
def login(smtpDomainName, smtpPortNumber, username, password):
	smtpObj = smtplib.SMTP(smtpDomainName, smtpPortNumber)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(username, password)
	return smtpObj

# EFFECTS: Sends a reply via Gmail.
def sendReplyGmail(recipient, subject, content):
	smtpObj = login('smtp.gmail.com', 587, email_setup.GMAIL_USERNAME, email_setup.GMAIL_PASSWORD)
	smtpObj.sendmail(email_setup.GMAIL_USERNAME, recipient, 'Subject: ' + subject + '\n' + content)
	smtpObj.quit()

# EFFECTS: Sends a reply via Outlook.
def sendReplyOutlook(recipient, subject, content):
	smtpObj = login('smtp-mail.outlook.com', 587, email_setup.OUTLOOK_USERNAME, email_setup.OUTLOOK_PASSWORD)
	smtpObj.sendmail(email_setup.OUTLOOK_USERNAME, recipient, 'Subject: ' + subject + '\n' + content)
	smtpObj.quit()


# EFFECTS: Sends a reply via Umich email.
def sendReplyUMich(recipient, subject, content):
	smtpObj = login('smtp.gmail.com', 587, email_setup.UMICH_USERNAME, email_setup.UMICH_PASSWORD)
	smtpObj.sendmail(email_setup.UMICH_USERNAME, recipient, 'Subject: ' + subject + '\n' + content)
	smtpObj.quit()

# REQUIRES: The email type.
# EFFECTS: Returns true if input email macro is valid.
def checkValidEmail(email):
	return email == OUTLOOK | email == UMICH | email == GMAIL
