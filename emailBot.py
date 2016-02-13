# Name: Zheng Hao Tan
# Email: tanzhao@umich.edu
# Date: May 16, 2015

# This program is to be used in conjunction with my Task Scheduler Bot that runs
# as a daemon for handling other tasks, including my emails.

# USAGE: python3 emailBot.py <OUTLOOK, UMICH, GMAIL>

import os, re, logging, sys
import smtplib

# Load usernames and passwords.
os.system('source ~/secrets.sh')

UMICH_USERNAME = os.environ.get("UMICH_USERNAME")
UMICH_PASSWORD = os.environ.get("UMICH_PASSWORD")

OUTLOOK_USERNAME = os.environ.get("OUTLOOK_USERNAME")
OUTLOOK_PASSWORD = os.environ.get("OUTLOOK_PASSWORD")

GMAIL_USERNAME = os.environ.get("GMAIL_USERNAME")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

# EFFECTS: Logs in to the appropriate email provider.
def loginEmail(emailAddress):
	if emailAddress == GMAIL:
		loginGmail(emailAddress)
	elif emailAddress == OUTLOOK:
		loginOutlook(emailAddress)
	elif emailAddress == HOTMAIL:
		loginGmail(emailAddress)

# EFFECTS: Sends a reply based on the email address, subject and content provided.
def sendReply(emailAddress, recipient, subject, content):
	if emailAddress == 'GMAIL':
		sendReplyGmail(recipient, subject, content)
	elif emailAddress == 'OUTLOOK':
		sendReplyOutlook(recipient, subject, content)
	elif emailAddress == 'UMICH':
		sendReplyUMich(recipient, subject, content)

# EFFECTS: Sends a reply via Gmail.
def sendReplyGmail(recipient, subject, content):
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(GMAIL_USERNAME, GMAIL_PASSWORD)
	smtpObj.sendmail(GMAIL_USERNAME, recipient, 'Subject: ' + subject + '\n' + content)
	smtpObj.quit()


# EFFECTS: Sends a reply via Outlook.
def sendReplyOutlook(recipient, subject, content):
	smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(OUTLOOK_USERNAME, OUTLOOK_PASSWORD)
	smtpObj.sendmail(OUTLOOK_USERNAME, recipient, 'Subject: ' + subject + '\n' + content)
	smtpObj.quit()


# EFFECTS: Sends a reply via Umich email.
def sendReplyUMich(recipient, subject, content):
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(UMICH_USERNAME, UMICH_PASSWORD)
	smtpObj.sendmail(UMICH_USERNAME, recipient, 'Subject: ' + subject + '\n' + content)
	smtpObj.quit()

# EFFECTS: Returns true if input email macro is valid.
def checkValidEmail(email):
	return email == OUTLOOK | email == UMICH | email == GMAIL

#def main():

subject = 'lalala header'
body = 'lalala body'


# Sends the reply
print('Sending reply...')
sendReply('OUTLOOK', UMICH_USERNAME, subject, body)
print('Reply sent!')

	# Command line argument handling.
	#for email in sys.argv[1:]:

	#	if checkValidEmail(email) == None:
	#		print('There is something wrong with the email provided.')
	#		print('Please rerun the program again')
	#		sys.exit()

	#	print('Currently handling ' + email + '...')

	#	#TODO
	#	loginEmail(email)


	#	print('Done with ' + email)

