import RPi.GPIO as GPIO
import Messenger
from time import sleep

GPIO.setmode(GPIO.BOARD)

ledGreenPin = 12
ledRedPin = 18
buttonMessage1 = 11
buttonMessage2 = 13
buttonMessage3 = 15

GPIO.setup(ledRedPin, GPIO.OUT)
GPIO.setup(ledGreenPin, GPIO.OUT)
GPIO.setup(buttonMessage1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonMessage2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonMessage3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    button1State = GPIO.input(buttonMessage1)
    button2State = GPIO.input(buttonMessage2)
    button3State = GPIO.input(buttonMessage3)
    if not button1State or not button2State or not button3State:
        if not button1State:
            message = "Message for button 1"
        elif not button2State:
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