import RPi.GPIO as GPIO
import mcp3008
import datetime

class PiGardenFunctions:
    def __init__(self,valvepin=16):
        self.valvepin = valvepin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.valvepin, GPIO.OUT)
        GPIO.output(self.valvepin, False)
    def openvalve(self):
        GPIO.output(self.valvepin, True)
    def closevalve(self):
        GPIO.output(self.valvepin, False)
    def getmoisture(self):
        mcp3008.readadc(5)
    def gethour(self):
        return datetime.datetime.now().time().hour
    def getminutes(self):
        return datetime.datetime.now().time().minutes 
    def iswet(self):
        pass
