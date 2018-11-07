import sys

from car import Car
from manager import Manager


def handle_invalid_input():
    print('### ERROR ###')
    print('that was an invalid input! aborting!!!')


text = ''
manager = Manager()


def handle_car_input():
    print('please enter the data for your car:')
    print('*** please enter the brand: ')
    brand = input()

    if len(brand) <= 0:
        handle_invalid_input()
        sys.exit()

    print('*** please enter the model: ')
    model = input()
    if len(model) <= 0:
        handle_invalid_input()
        sys.exit()

    print('*** please enter the year (4 digits): ')
    year = input()
    if not year.isdigit() or len(year) < 4:
        handle_invalid_input()
        sys.exit()

    print('*** please enter the power (>0): ')
    power = input()
    if not power.isdigit() or int(power) < 0:
        handle_invalid_input()
        sys.exit()

    car = Car(make=brand, model=model, year=int(year), pwr=int(power))
    manager.add(car)


while text != 'c':
    text = input('please enter your command: [a]dd, [p]rint, [e]mpty, [l]ength or [c]ancel')

    if text == 'a':
        handle_car_input()

    elif text == 'p':
        print(manager)
    elif text == 'e':
        manager.clear()
    elif text == 'l':
        print('length of manager: ' + str(len(manager)))
    elif text == 'c':
        sys.exit(0)
