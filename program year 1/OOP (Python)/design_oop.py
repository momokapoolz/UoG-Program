from oop_system import Light
from oop_system import Heating
from oop_system import Music_Player

led_light = Light() #define the object off a class by assigning constructor function
#print class light attribute
print(led_light.name, led_light.type, led_light.level, led_light.status)
#call the method of light class
led_light.turn_on()
led_light.increase()


#heating
panasonic_heat = Heating()
print(panasonic_heat.name, panasonic_heat.type, panasonic_heat.level, panasonic_heat.status)
panasonic_heat.turn_on
panasonic_heat.decrease


#music player
sony_mp3 = Music_Player()
print(sony_mp3.name, sony_mp3.level, sony_mp3.songs, sony_mp3.status)
sony_mp3.play()
sony_mp3.next()
sony_mp3.pause()

def chosen(device, command):
    if device in command or device.replace(" ", "") in command:
        return True
    else:
        return False


#them device
def init_devices():
    devices = [led_light, panasonic_heat, sony_mp3]

    for device in devices:
        print(f"{device.name} has been initiallised")
    
    return devices


#command cho cac devices
def control_devices(device, command, name):
    if " on " in command:
        device.turn_on()
        print(device + " is on")
    elif " off " in command:
        device.turn_off()
        print(device + " is off")
    elif " up " in command:
        device.increase()
    elif " down " in command:
        device.decrease()
    elif " play " in command and device == "sony_mp3":
        device.play()
    elif " pause " in command and device == "sony_mp3":
        device.pause()
    else:
        print(f"Sorry {name}, I do not understand that")


#main 
dv = init_devices()


