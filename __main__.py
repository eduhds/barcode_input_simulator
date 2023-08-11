import sys
import json
import random
from pynput import keyboard

opt_file = '-f'
opt_list = '-l'


def show_help():
    print('--- Invalid command ---')
    print('\tValid options are:')
    print('\t• -f filename.json')
    print('\t• -l code1 code2 code3 ...')


def show_help_for_f():
    print('--- Invalid command for "{0}" ---'.format(opt_file))
    print('\tFile must be JSON format with array of string codes.')
    print('\t• Example:')
    print(
        '\tA file named "codes.json" with content like ["code1", "code2", "code3"]')


def show_help_for_l():
    print('--- Invalid command for "{0}" ---'.format(opt_list))
    print('\tArgs must be list of codes.')
    print('\t• Example:')
    print('\t-l code1 code2 code3 ...')


if len(sys.argv) < 2:
    show_help()
    exit(1)

option = sys.argv[1]
data = None
value_index = 0

if option == opt_file:
    if len(sys.argv) != 3 or not sys.argv[2].endswith('.json'):
        show_help_for_f()
        exit(1)

    file = open(sys.argv[2])

    data = json.load(file)

    file.close()

    if type(data) is not list:
        show_help_for_f()
        exit(1)
elif option == opt_list:
    if len(sys.argv) < 3:
        show_help_for_l()
        exit(1)

    data = sys.argv[2:]
else:
    show_help()
    exit(1)

if data == None:
    print('Error')
    exit()

controller = keyboard.Controller()


def random_value_from_data():
    index = random.randint(0, len(data)-1)
    return data[index]


def next_value_from_data():
    global value_index
    next_value = data[value_index]
    value_index = value_index+1
    return next_value


def on_press(key):
    # try:
    #    print('alphanumeric key {0} pressed'.format(key.char))
    # except AttributeError:
    #    print('special key {0} pressed'.format(key))
    return


def on_release(key):
    global value_index

    if key == keyboard.Key.f2:
        value = next_value_from_data()  # random_value_from_data()
        controller.type('{0}\n'.format(value))
        # print('{0} released with value {1}'.format(key, value))
        print('• {0} released'.format(value))

        if value_index > (len(data)-1):
            print('All codes released, exiting.')
            return False

    if key == keyboard.Key.esc:
        print('Esc pressed, exiting.')
        return False


print('Running... Press ESC to exit or F2 to release input code.')

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
