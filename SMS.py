import twilio
import requests
import bs4

URL = 'http://apply.co.zw/'
MESSAGE = 'Apply Zimbabwe added a new opportunity!'

def main():

    f = open('log.txt', 'r')
    current = f.readlines()
    f.close()

    if (scrapeSite(URL, current) is True):
        SMS()


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

def SMS():
    try:
        account_sid = "ACb8d67922605d8e4d22134bbbe8f3a319"
        auth_token = "18ffe2ba3721b596b8aee41c19818f6e"
        client = (account_sid, auth_token)
        message = client.messages.create(
            to="+13302016997",
            from_="+13307654154",
            body="Check your calendar for your next appointment Tanaka",
            media_url="https://climacons.herokuapp.com/clear.png")
        print('Success! message ID: ' + message.sid)

    except twilio.TwilioRestException as e:
        print(e)

if __name__ == "__main__": main()

SMS()
