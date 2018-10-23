def calc_factorial(n: int):
    if n == 0:
        return 1
    fact = n
    if n < 0:
        raise ValueError('factorial is not defined for negative numbers!')
    if isinstance(n, float):
        raise ValueError('factorial only accepts fixed-point numbers!')
    for i in range(1, n, 1):
        fact *= i

    return fact


def is_invalid_input(text: str):
    return isinstance(text, float) or (not text.isdigit()) or text.isspace()


def run():
    number = input('enter number for the factorial computation: ')
    if is_invalid_input(number):
        print('invalid input. restart to try again')
    else:
        print('factorial is ' + str(calc_factorial(int(number))))
