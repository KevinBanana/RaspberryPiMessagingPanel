from twilio.rest import Client
import config
import sys


def send_message(message):
    # The following line needs your Twilio Account SID and Auth Token
    client = Client(config.SID, config.AUTH_TOKEN)

    client.messages.create(to=config.KEVIN_NUMBER,
                           from_=config.TWILIO_NUMBER,
                           body=message)


if __name__ == "__main__":
    message = sys.argv[1]
    send_message(message)
