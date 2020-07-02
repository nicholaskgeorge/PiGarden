from PiGardenFunctions import PiGardenFunctions

garden = PiGardenFunctions()
#allow for automatic times to be set. Each element in the list contains a tuple of the
#hour and minute in 24 hour time.;+++++++++
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
    if command == 'start':
        garden.start()
    elif command == 'stop':
        pass
    elif command == 'wsettings':
        print("""
                 \n***COMANDS***
                 \nseeset- lets you see the current Settings
                 \ndefault- reverts to default Settings
                 \nwaterduration- change how long valvue stays open each application (in seconds)
                 \nwatertimes- change times that watering happens each day
            """)
    elif command == 'schedule':
        pass
    elif command == 'waternow':
        garden.water()
    elif command == 'default':
        garden.default()
    else:
        print("Sorry your that isn't a command")

def settingings():
    command = raw_input("Type your command here ---> ")
    if command == 'seeset':
        return 
