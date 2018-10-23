def to_binary(number: int) -> str:
    if isinstance(number, float):
        raise ValueError

    if isinstance(number, str):
        raise ValueError

    if number == 0:
        return "0"
    s = ''
    while number > 0:
        if number & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        number //= 2
    return s


def is_invalid_input(text: str):
    return isinstance(text, float) or (not text.isdigit()) or text.isspace()


def run():
    number = input('please enter a positive integer: ')

    if is_invalid_input(number):
        print('invalid input. restart to try again')
    else:
        print(to_binary(int(number)))
