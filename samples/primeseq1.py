from primecheck import is_prime


def print_primes(upper: int):
    count = 0
    for i in range(0, upper, 1):
        if is_prime(i):
            print(str(count) + ') prime number found: ' + str(i))
            count += 1


def is_invalid_input(text: str):
    return isinstance(text, float) or (not text.isdigit()) or text.isspace()


def run():
    number = input('enter number for the prime sequence computation: ')
    if is_invalid_input(number):
        print('invalid input. restart to try again')
    else:
        print('factorial is ' + str(print_primes(int(number))))


