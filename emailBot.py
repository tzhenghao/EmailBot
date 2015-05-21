# Name: Zheng Hao Tan
# Email: tanzhao@umich.edu
# Date: May 16, 2015

# This program is to be used in conjunction with my Task Scheduler Bot that runs
# as a daemon for handling other tasks, including my emails.

import os, re, logging, sys, pyperclip

# Handle my personal Gmail account.
def gmailHandler(GMAIL):
	return True
# Handle my Hotmail.
def hotmailHandler(HOTMAIL):
	return True
# Handle my Umich account.
def UMichHandler(UMICH):
	return True

def isLoginGmail(email):
	return True

def isLoginHotmail(email):
	return True

def isLoginUmich(email):
	return True

# EFFECTS: Checks for email type. Returns true on success; false on failure.
def checkEmail(email):
	if isLoginGmail(email):
		return gmailHandler(email)
	elif isLoginHotmail(email):
		return hotmailHandler(email)
	elif isLoginUmich(email):
		return UMichHandler(email)
	else:
		return False

# Command line argument handling.
for email in sys.argv[1:]:

	print('Currently handling ' + email + '...')

	if checkEmail(email) == None:
		print('There is something wrong with the email provided.')
		print('Please rerun the program again')
		sys.exit()
