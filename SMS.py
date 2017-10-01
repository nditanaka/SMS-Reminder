# Sending an SMS using the Twilio API
from twilio.rest import Client
# put your own credentials here
account_sid = "AC5ef872f6da5a21de157d80997a64bd33"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)
client.messages.create(
  to="+13302016997",
  from_="+13307654154",
  body="Check your calendar for your next appointment Tanaka",
  media_url="https://climacons.herokuapp.com/clear.png")
