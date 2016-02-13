# Name: Zheng Hao Tan
# Email: tanzhao@umich.edu
# Date: May 16, 2015

# This program is to be used in conjunction with my Task Scheduler Bot that runs
# as a daemon for handling other tasks, including my emails.

# USAGE: python3 emailBot.py <OUTLOOK, UMICH, GMAIL>

import os, re, logging, sys, pyperclip
import gmail, yagmail

from myutils import get_myenv

myenv = get_myenv()

# Load usernames and passwords.
UMICH_USERNAME = myenv['UMICH_USERNAME']
UMICH_PASSWORD = myenv['UMICH_PASSWORD']

OUTLOOK_USERNAME = myenv['OUTLOOK_USERNAME']
OUTLOOK_PASSWORD = myenv['OUTLOOK_PASSWORD']

GMAIL_USERNAME = myenv['GMAIL_USERNAME']
GMAIL_PASSWORD = myenv['GMAIL_PASSWORD']

# EFFECTS: Logs in to the appropriate email provider.`
def loginEmail(emailAddress):
	if (emailAddress == GMAIL):
		loginGmail(emailAddress)
	elif (emailAddress == OUTLOOK)
		loginOutlook(emailAddress)
	elif (emailAddress == HOTMAIL)
		loginGmail(emailAddress)

# EFFECTS: Sends a reply based on the email address, subject and content provided.
def sendReply(emailAddress, recipient, subject, content):
	if (emailAddress == GMAIL):
		sendReplyGmail(recipient, subject, content)
	elif (emailAddress == OUTLOOK)
		sendReplyOutlook(recipient, subject, content)
	elif (emailAddress == HOTMAIL, subject, content)
		sendReplyUMich(recipient, subject, content)

# EFFECTS: Sends a reply via Gmail.
def sendReplyGmail(recipient, subject, content):
	yagmail.register(GMAIL_USERNAME, GMAIL_PASSWORD)
	yag = yagmail.SMTP(GMAIL_USERNAME)
	yag.send(
		to=recipient,
		subject='RE: {}'.format(subject),
		contents=content
	)


# EFFECTS: Sends a reply via Outlook.
def sendReplyOutlook(recipient, subject, contents):

# EFFECTS: Sends a reply via Umich email.
def sendReplyUMich(recipient, subject, contents):
	yagmail.register(UMICH_USERNAME, UMICH_PASSWORD)
	yag = yagmail.SMTP(UMICH_USERNAME)
	yag.send(
		to=recipient,
		subject='RE: {}'.format(subject),
		contents=content
	)

# EFFECTS: Returns true if input email macro is valid.
def checkValidEmail(email):
	return email == OUTLOOK || email == UMICH || email == GMAIL

def main():
	# Command line argument handling.
	for email in sys.argv[1:]:

		if checkValidEmail(email) == None:
			print('There is something wrong with the email provided.')
			print('Please rerun the program again')
			sys.exit()

		print('Currently handling ' + email + '...')

		#TODO
		loginEmail(email)


		print('Done with ' + email)

