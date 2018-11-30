pi = 3.746
myint: int = int(pi)
print('via int convertion: ', myint)
print('via round: ', round(pi, 0))


def print_stars_in_one_line(num_stars):
    # if num_stars > 10:
    #     print('sorry, can only print maximum of 10 stars!')
    #     return

    for elem in range(num_stars):
        print('*', end='')
    print()

    # also possible:
    # print('*' * num_stars)


# stars = input('enter the number of stars: ')
# print_stars(int(stars))
# print('done')

for stars in range(20):
    print_stars_in_one_line(stars)
