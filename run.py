import email_setup
import email_send
import email_receive

# Initialize environment variables.
email_setup.init()

# EFFECTS: Sends out the email.
subject = 'lalala header'
body = 'lalala body'

print('How are you today?')

print('What would you like to do?')

# Sends the reply
print('Sending reply...')
email_send.sendReply('UMICH', email_setup.UMICH_USERNAME, subject, body)
print('Reply sent!')
