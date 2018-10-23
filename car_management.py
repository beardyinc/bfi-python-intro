import sys

print('please enter the data for your car:')
print('*** please enter the brand: ')
brand = input()


def handle_invalid_input():
    print('### ERROR ###')
    print('that was an invalid input! aborting!!!')


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

car = {
    "model": model,
    "brand": brand,
    "year": year,
    "power (hp)": power
}

print(car)
