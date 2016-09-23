#!/usr/local/bin/python3

import os
import re
import logging
import sys
import smtplib

class Email(object):

  def __init__(self, username, password):
    self.username = username
    self.password = password

  # REQUIRES: A recipient (another email), subject and body.
  # EFFECTS: Sends an email to the given recipient with the given subject and body.
  def send(self, recipient, subject, body):
    self.smtpObj.sendmail(self.username, recipient, 'Subject: ' + subject + '\n' + body)

class Gmail(Email):
  def __init__(self, username, password, SMTPServerDomainName = 'smtp.gmail.com',
               SMTPServerPort = '587'):

    self.SMTPServerDomainName = SMTPServerDomainName
    self.SMTPServerPort = SMTPServerPort
    super(Gmail, self).__init__(username, password)

    # attempt to login.
    self.smtpObj = smtplib.SMTP(SMTPServerDomainName, SMTPServerPort)
    self.smtpObj.ehlo()
    self.smtpObj.starttls()
    self.smtpObj.login(username, password)

class Outlook(Email):
  def __init__(self, username, password,
               SMTPServerDomainName = 'smtp-mail.outlook.com',
               SMTPServerPort = '587'):
    self.SMTPServerDomainName = SMTPServerDomainName
    self.SMTPServerPort = SMTPServerPort
    super(Outlook, self).__init__(username, password)

# TODO: More email providers.
#class ICloud(Email):
#	def __init__(self):
#		self.SMTPServerDomainName = 'smtp.gmail.com'
#		self.SMTPServerPort = 587
#
