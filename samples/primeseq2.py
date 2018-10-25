from primecheck import is_prime


def get_primes(upper: int) -> list:
    count = 0
    result = []
    for i in range(0, upper, 1):
        if is_prime(i):
            result.append(i)
            count += 1
    return result


def is_invalid_input(text: str):
    return isinstance(text, float) or (not text.isdigit()) or text.isspace()


def run():
    number = input('enter number for the prime sequence computation: ')
    if is_invalid_input(number):
        print('invalid input. restart to try again')
    else:
        print('factorial is ' + str(get_primes(int(number))))


