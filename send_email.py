#!/usr/local/bin/python3

import Email

# EFFECTS: Sends out the email.
subject = 'This is a test header'
body = 'This is a test body'

gmail = Email.Gmail(<username>, <password>)

print('How are you today?')

print('What would you like to do?')

# Sends the reply
print('Sending reply...')
gmail.send("oxalate94@hotmail.com", subject, body)
print('Reply sent!')
