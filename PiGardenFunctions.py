import RPi.GPIO as GPIO
import mcp3008
import datetime

class PiGardenFunctions:
    def __init__(self,valvepin=16,wetthreshold=430, watertime=5):
        self.wetthreshold = wetthreshold
        self.valvepin = valvepin
        self.watertime = watertime
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.valvepin, GPIO.OUT)
        GPIO.output(self.valvepin, False)
    def openvalve(self):
        print('Opening Valve')
        GPIO.output(self.valvepin, True)
    def closevalve(self):
        print('Closing Valve')
        GPIO.output(self.valvepin, False)
    def getmoisture(self):
        mcp3008.readadc(5)
    def gethour(self):
        return datetime.datetime.now().time().hour
    def getminutes(self):
        return datetime.datetime.now().time().minutes
    def iswet(self):
        #The more moist the soil is the lower the value that is recived
        return False if self.wetthreshold>getmoisture() else True
    def water(self):
        moisture = 0
        count = 0
        #taking an avergae to acount for measurement error
        for i in range(10):
            moisture+=self.getmoisture()
        moisture//=10
        print('Starting watering')
        # We will keep watering until the soil is moist. There is a count in case
        # something has gone wrong with the sensor and all the water is drained
        while not iswet() and count<8:
            self.openvale()
            time.sleep(self.watertime)
            self.closevalve()
            count+=1
        print('Watering finished')
