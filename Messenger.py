from twilio.rest import Client
import config

# the following line needs your Twilio Account SID and Auth Token
client = Client(config.SID, config.AUTH_TOKEN)

client.messages.create(to=config.JULES_NUMBER,
                       from_=config.TWILIO_NUMBER,
                       body="Hello it's me Kevin")