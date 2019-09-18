#! python3
# textme.py - Helper function to send notification to my number.

import os
from twilio.rest import TwilioRestClient

# Reading account details from environment variable":
accSID = os.environ.get('tw_SID')
token = os.environ.get('tw_token')
receiverNumber = os.environ.get('tw_receiver')
senderNumber = os.environ.get('tw_sender')

def textme(message):
	twCli = TwilioRestClient(accSID, token)
	twCli.messages.create(body=message, from_=senderNumber, to=receiverNumber)


if __name__ == '__main__':
	textme()
