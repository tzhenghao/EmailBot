# This Python script will attempt to login to all relevant email accounts
# and load all system environment variables.

import os

# EFFECTS: Load usernames and passwords from current environment.
def init():
	os.system('source ~/.secrets.sh')

	global UMICH_USERNAME, UMICH_PASSWORD
	global OUTLOOK_USERNAME, OUTLOOK_PASSWORD
	global GMAIL_USERNAME, GMAIL_PASSWORD

	UMICH_USERNAME = os.environ.get("UMICH_USERNAME")
	UMICH_PASSWORD = os.environ.get("UMICH_PASSWORD")

	OUTLOOK_USERNAME = os.environ.get("OUTLOOK_USERNAME")
	OUTLOOK_PASSWORD = os.environ.get("OUTLOOK_PASSWORD")

	GMAIL_USERNAME = os.environ.get("GMAIL_USERNAME")
	GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")