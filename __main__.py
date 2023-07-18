import sys
import json
import random
from pynput import keyboard


file = open(sys.argv[1])

data = json.load(file)

file.close()

controller = keyboard.Controller()


def random_value_from_data():
    index = random.randint(0, len(data)-1)
    return data[index]


def on_press(key):
    # try:
    #    print('alphanumeric key {0} pressed'.format(key.char))
    # except AttributeError:
    #    print('special key {0} pressed'.format(key))
    return


def on_release(key):
    if key == keyboard.Key.f2:
        value = random_value_from_data()
        controller.type('{0}\n'.format(value))
        print('{0} released with value {1}'.format(key, value))

    if key == keyboard.Key.esc:
        return False


print('Running...')

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
