# Name: Zheng Hao Tan
# Email: tanzhao@umich.edu
# Date: Feb 14, 2016

# This Python script is responsible for IMAP calls and receiving unread emails.
import os, sys
import imapclient
import email_setup

# EFFECTS: Logs in to the specified email address.
def login(imapDomainName, imapPortNumber, username, password):
	imapObj = imapclient.IMAPClient(imapDomainName, ssl=True)
	imapObj.login(username, password)
	return imapObj

# EFFECTS: Retrieves the folder from the specified email address.
def retrieveFolder(imapObj, retrieveFolder)
	imapObj = select_folder(retrieveFolder, readonly=True)

imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Mar-2016'])

