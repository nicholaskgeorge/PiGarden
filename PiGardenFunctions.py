import RPi.GPIO as GPIO
import mcp3008
import datetime

class PiGardenFunctions:
    def __init__(self):
        #the wet threshold will need to be found experimentally this is
        #just a value I found online
        self.wetthreshold=0
        #pin where we connect the pi to the relay
        self.valvepin=0
        #this is how long the valve will stay open at anytime we water
        self.waterduration=0
        #set times of day to water plants. Stores hour and minutes in tuples
        self.watertimes=[]
        #number of days per week to waters
        self.daysperweek=0
        #List of 7 integears either 0 or 1 corresponding to each day. Determins whether to water or not
        self.waterdays=[]
        #data is pulled from a file which holds settings
        self.updatefromfile()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.valvepin, GPIO.OUT)
        #making the valve start off closed
        GPIO.output(self.valvepin, False)
    def openvalve(self):
        print('Opening Valve')
        GPIO.output(self.valvepin, True)
    def closevalve(self):
        print('Closing Valve')
        GPIO.output(self.valvepin, False)
    def getmoisture(self):
        #the 5 here corresponds to the port on the mcp3008 chip which converts
        #analog to digital.
        mcp3008.readadc(5)
    def gethour(self):
        return datetime.datetime.now().time().hour
    def getminutes(self):
        return datetime.datetime.now().time().minutes
    def iswet(self):
        #The more moist the soil is the lower the value that is recived
        return False if self.wetthreshold>getmoisture() else True
    #only waters if the soil is wet
    def water(self):
        moisture = 0
        count = 0
        #taking an avergae to acount for measurement error
        for i in range(10):
            moisture+=self.getmoisture()
        moisture//=10
        if not iswet():
            print('Starting watering')
            #We will keep watering until the soil is moist. There is a count in case
            #something has gone wrong with the sensor. This stops all the water
            #getting drained
            while not iswet() and count<8:
                self.openvale()
                time.sleep(self.watertime)
                self.closevalve()
                time.sleep(3)
                count+=1
            print('Watering finished')
        else:
            print('Soil is already wet')

    #This function decides what days to water the plants on based on the amount
    #of times per week the user has indicated. Returns a list of 7 booleans
    #indicating whether it is a day to water or not
    def calculatewaterdays(self):
        days = [False]*7
        #spreads out water days as evenly as possible
        for i in range(7,step=7//daysperweek):
            days[i] = True
        return days

    #returns True if it is a watering day, otherwise False
    def daytowater(self):
        #gets date in day/month/year format
        today = date.today.strftime("%d/%m/%Y")
        #gets the number of the day of the week. NOTE: Monday corresponds to the
        #zeroth day of the week
        day = datetime.datetime.strptime(today, '%d/%m/%Y').weekday()
        #Returns whether the day is a watering day
        return waterdays[day]

    def automated(self):
        while True:
            #If it is just waiting we can give it really long delays to save
            #save computing power
            time.sleep(55)
            if daytowater():
                if (self.gethour(),self.getminutes()) in self.watertimes:
                    self.water()
    #function will start the automation thread
    def start(self):
        pass
    #Reads file and updates settings into instance variables
    # settings are stored in the folllowing line order:
    # 1.waterduration
    # 2.daysperweek
    # 3.waterdays
    def updatefromfile(self):
        settings = open('Settings.txt','r')
        raw = file.readlines()
        file.close
        #parsing line by line and gets data
        lines = raw.split('\n')
        line1=lines[0]
        waterduration = int(line1[line1.find(':')+1:].strip())
        line2 = lines[1]
        daysperweek = int(line2[line2.find(':')+1:].strip())
        line3 = lines[2]
        waterdays=line3[line3.find(':')+1:]
        waterdays = waterday.strip().split(' ')
        line4 = lines[3]
        #applying read data
        self.waterduration = waterduration
        self.daysperweek = daysperweek
        self.waterdays = waterdays
        watertimes = []
        rawlist= line4.strip().split(' ')
        for i in rawlist:
            colon = i.find(':')
            watertimes += (i[:colon],i[colon+1:])
        self.watertimes = watertimes

    def defaultsettings(self):
        self.changewaterduration(5)
        self.changewatertimes([(6:30),(19:00)])
        self.changedaysperweek(7)
        self.changewaterdays([1,1,1,1,1,1,1])
    #functions to change Settings
    def changewaterduration(self, time):
        self.waterduration = time
        settings = open('Settings.txt','r')
        raw = file.readlines()
        file.close
        lines = raw.split('\n')
        lines[0] = "waterduration: "+string(time)
        updated = ''.join(lines)
        settings = open('Settings.txt','w')
        settings.write(updated)
        settings.close()
    #must be passed a list of times with the hours and minutes in a tuple
    def changewatertimes(self, times):
        self.waterduration = times
        settings = open('Settings.txt','r')
        raw = file.readlines()
        file.close
        lines = raw.split('\n')
        newtime = ''
        for i in times:
            newtime = string(i[0])+":"+string(i[1])+" "
        lines[3]= "watertimes: "+newtime
        updated = ''.join(lines)
        settings = open('Settings.txt','w')
        settings.write(updated)
        settings.close()

    def changedaysperweek(self, numdays):
        self.changedaystowater = numdays
        settings = open('Settings.txt','r')
        raw = file.readlines()
        file.close
        lines = raw.split('\n')
        lines[1] = "daysperweek: "+string(numdays)
        updated = ''.join(lines)
        settings = open('Settings.txt','w')
        settings.write(updated)
        settings.close()
    #must be given a list of length 7 which each element being a 1 or a zero
    def changewaterdays(self, days):
        self.waterduration = times
        settings = open('Settings.txt','r')
        raw = file.readlines()
        file.close
        lines = raw.split('\n')
        newdays = ''
        for i in days:
            days = string(i)+' '
        lines[2]= "waterdays: "+newtime
        updated = ''.join(lines)
        settings = open('Settings.txt','w')
        settings.write(updated)
        settings.close()
