from PiGardenFunctions import PiGardenFunctions

garden = PiGardenFunctions()
#allow for automatic times to be set. Each element in the list contains a tuple of the
#hour and minute in 24 hour time.
settimes = [(7,0)]
waterperday=1
waterperweek=7
print("""Hello! Welcome to AutoGarden. Here you can change and customize the settings
       \n once you have all the parts connected, type the following commands in order to customize the system""")
while True:
    print("""
             \n***COMANDS***
             \nstart - Starts automated irrigation
             \nstop - Stops automated irrigation
             \nwsettings - Watering settings
             \nschedule- Change timing and frequency of watering
             \nwaternow - forces a watering session regardless of moisutre
             \ndefault - resets setting to the default recommended settings
        """)
    command = raw_input("Type your command here ---> ")
