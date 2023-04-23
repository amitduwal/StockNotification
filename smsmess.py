from twilio.rest import Client

from dotenv import load_dotenv
import os
load_dotenv() 

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)
message = client.messages.create(
    body='Hello, world!',
    from_='+19787170614',  # replace with your Twilio phone number
    to='+9779860916899'  # replace with the recipient's phone number
)

print(message.sid)
