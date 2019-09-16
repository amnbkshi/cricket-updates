#! python3
# textme.py - Helper function to send notification to my number.

import os
from twilio.rest import TwilioRestClient

# Reading account details from environment variable":
accSID = os.env.get('tw_SID')
token = os.env.get('tw_token')
receiverNumber = os.env.get('tw_receiver')
senderNumber = os.env.get('tw_sender')

def textme(message):
	twCli = TwilioRestClient(accSID, token)
	twCli.messages.create(body=message, from_=senderNumber, to=receiverNumber)


if __name__ == '__main__':
	textme()
