import sys

from converter import Converter

conv = Converter()

inpt = ''

while inpt != 'q':
    inpt = input(
        'enter for conversion\n[f] celsius to fahrenheit\n[c] fahrenheit to celsius\n[b] number to binary\n[q]quit: ')
    val = input('now input the value: ')
    if inpt == 'f':
        print(conv.celsius_to_fahrenheit(int(val)))
    elif inpt == 'c':
        print(conv.fahrenheit_to_celsius(int(val)))

    elif inpt == 'b':
        print(conv.num_to_binary(int(val)))

    elif inpt == 'q':
        sys.exit(0)
