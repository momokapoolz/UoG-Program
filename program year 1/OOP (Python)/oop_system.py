def chosen(device, command):
    if device in command or device.replace(" ", "") in command:
        return True
    else:
        return False


device_names = []
device_ons = []
device_settings = []
device_types = []

def init_devices(device_names, device_ons, device_settings, device_types):
    device_names.append("heating")
    device_names.append("ceiling light")
    device_names.append("music player")
    device_names.append("movie player")

    device_ons.append(False)
    device_ons.append(False)
    device_ons.append(False)
    device_ons.append(False)

    device_settings.append(18)
    device_settings.append(350)
    device_settings.append(7)
    device_settings.append(6)

    device_types.append("temperature")
    device_types.append("brightness")
    device_types.append("volume")
    device_types.append("movie")

    for device in device_names:
        print(f"{device} has been initialised")



def init_name():
    name = input("What is your name? ")
    print(f"Hello {name}")
    return name

def control_devices(device, command, name):
    i = device_names.index(device)
    if " on " in command:
        device_ons[i] = True
        print(device + " is on")
    elif " off " in command:
        device_ons[i] = False
        print(device + " is off")
    elif " up " in command:
        device_settings[i] += 1
        print(f" {device} {device_types[i]} is set to {device_settings[i]}")
    elif " down " in command:
        device_settings[i] -= 1
        print(f" {device} {device_types[i]} is set to {device_settings[i]}")
    elif " play " in command and device == "music player":
        print(f" {device} is playing")
    elif " pause " in command and device == "music player":
        print(f" {device} is paused")
    else:
        print(f"Sorry {name}, I do not understand that")


def main():
    init_devices(device_names, device_ons, device_settings, device_types)
    name = init_name()
    while True:
        print()
        command = input(f"What next, {name}? ")
        command = f" {command.lower()} "

        if "system off" in command:
            break

        device_chosen = None
        for device in device_names:
            if chosen(device, command):
                device_chosen = device
                break

        if device_chosen is None:
            print(f"Sorry {name}, I do not understand that")
        else:
            control_devices(device, command, name)
            print(f"Bye bye, {name}")
main()