import os
import RPi.GPIO as GPIO
import Messenger
from time import sleep

GPIO.setmode(GPIO.BOARD)

ledGreenPin = 12
ledRedPin = 18
buttonMessage1 = 16
buttonMessage2 = 11
buttonMessage3 = 13

GPIO.setup(ledRedPin, GPIO.OUT)
GPIO.setup(ledGreenPin, GPIO.OUT)
GPIO.setup(buttonMessage1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonMessage2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonMessage3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    button1State = GPIO.input(buttonMessage1)
    button2State = GPIO.input(buttonMessage2)
    button3State = GPIO.input(buttonMessage3)
    if button1State == False or button2State == False or button3State == False:
        # TODO: Get message based on dial
        if button1State == False:
            message = "Message for button 1"
        elif button2State == False:
            message = "Message for button 2"
        else:
            message = "Message for button 3"
        is_sent = Messenger.send_message(message)

        if is_sent:
            GPIO.output(ledGreenPin, GPIO.HIGH)
        else:
            GPIO.output(ledRedPin, GPIO.HIGH)

        sleep(.75)
    else:
        GPIO.output(ledRedPin, GPIO.LOW)
        GPIO.output(ledGreenPin, GPIO.LOW)