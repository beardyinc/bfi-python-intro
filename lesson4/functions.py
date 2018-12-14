def print_stars(num_stars):
    for i in range(num_stars):
        print('*', end='')
    print()


def my_sum(a, b):
    result = a + b
    return result


c = 4
d = 8
value = my_sum(c, d)
print('sum ', value)
print('type of value: ', type(value))
