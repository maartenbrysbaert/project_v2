from RPi import GPIO as GPIO
import time


class LedLamp:
    def __init__(self, buzzer=13):
        self.buzzer = buzzer
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buzzer, GPIO.OUT)

    def flikker(self, lengte):
        for i in range(lengte):
            GPIO.output(self.led, GPIO.HIGH)
            time.sleep(.3)
            GPIO.output(self.led, GPIO.LOW)
            time.sleep(.3)



#LedLamp().flikker(5)