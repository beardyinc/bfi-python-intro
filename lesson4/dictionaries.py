car = {
    'brand': 'bmw',
    'model': 'm4',
    'year': 2018,
    'engine': {
        'fuel': 'gasoline',
        'cylinders': 6,
        'bhp': 600
    },
    'inspections': [
        2018, 2019, 2020
    ]
}

# for key in car:
#     print('key: ', key)
#     print('value: ', car[key])
#
# for value in car.values():
#     print('value: ', value)
car['num_wheels']= 4
print(car)


print('bhp = ', car['engine']['bhp'])
# # is the same as:
#
# for curVal in car.values():
#     print('value: ', curVal)
#
# for key, val in car.items():
#     print('key: ', key, ', value: ', val)
#
#
#
