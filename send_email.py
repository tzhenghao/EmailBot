#!/usr/local/bin/python3

# Author: Zheng Hao Tan
# Email: tanzhao@umich.edu

import re
import sys
import Email

# Input validation
if len(sys.argv) != 6:
	print('Invalid arguments. Please rerun the script')
	sys.exit(1)

# Parse the username, password, recipient, subject and body.
username = sys.argv[1]
password = sys.argv[2]
recipient = sys.argv[3]
subject = sys.argv[4]
body = sys.argv[5]

#Check for the email type via regex.
emailTypeRegex = re.compile(r'@(gmail|outlook|hotmail|umich)')
emailType = emailTypeRegex.search(username)
emailType = emailType.group(1)

global mail

# Creates the email needed.
if emailType == 'gmail' or emailType == 'umich':
	mail = Email.Gmail(username, password)
elif emailType == 'outlook' or emailType == 'hotmail':
	mail = Email.Outlook(username, password)
else:
	sys.exit('Mail type not recognized!')

# Sends the reply
print('Sending reply...')
mail.send(recipient, subject, body)
print('Reply sent!')
