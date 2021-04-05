import os
import RPi.GPIO as GPIO
import Messenger
from time import sleep

GPIO.setmode(GPIO.BOARD)

ledGreenPin = 12
ledRedPin = 18
buttonPin = 16

GPIO.setup(ledRedPin, GPIO.OUT)
GPIO.setup(ledGreenPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    buttonState = GPIO.input(buttonPin)
    if buttonState == False:
        # TODO: Get message based on dial
        message = "test"
        is_sent = Messenger.send_message(message)

        if is_sent:
            GPIO.output(ledGreenPin, GPIO.HIGH)
        else:
            GPIO.output(ledRedPin, GPIO.HIGH)

        sleep(.75)
    else:
        GPIO.output(ledRedPin, GPIO.LOW)
        GPIO.output(ledGreenPin, GPIO.LOW)