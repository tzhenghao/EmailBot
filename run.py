import email_setup
import email_send

email_setup.init()

# EFFECTS: Sends out the email.
subject = 'lalala header'
body = 'lalala body'

# Sends the reply
print('Sending reply...')
email_send.sendReply('UMICH', email_setup.UMICH_USERNAME, subject, body)
print('Reply sent!')