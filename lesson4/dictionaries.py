car = {
    'brand': 'bmw',
    'model': 'm4',
    'power': 400,
    'year': 2018,
}

# print(car)
# print(car['brand'])

for key in car:
    val = car[key]
    print('key: ', key, ', value: ', val)

# is the same as:

for curVal in car.values():
    print('value: ', curVal)

for key, val in car.items():
    print('key: ', key, ', value: ', val)



