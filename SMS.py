import twilio
import requests
import bs4
import secrets


URL = 'http://apply.co.zw/'
MESSAGE = 'Apply Zimbabwe added a new opportunity!'


def main():

    f = open('log.txt', 'r')
    current = f.readlines()
    f.close()

    if (scrapeSite(URL, current) is True):
        sendAlert()


def scrapeSite(url, current):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    logo = soup.select('#hplogo')
    logo = logo[0]

    if logo['src'] != current:
        f = open('log.txt', 'w')
        f.write(logo['src'])
        return True

    return False

def sendAlert():
    try:
        client = twilio.rest.TwilioRestClient(secrets.TWILIO_ID, secrets.TWILIO_TOKEN)
        message = client.messages.create(
            to="+13302016997",
            from_="+13307654154",
            body="Check your calendar for your next appointment Tanaka",
            media_url="https://climacons.herokuapp.com/clear.png")
        print('Success! message ID: ' + message.sid)

    except twilio.TwilioRestException as e:
        print(e)

if __name__ == "__main__": main()

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
