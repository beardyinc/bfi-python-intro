class Converter:

    def num_to_binary(self, number: int) -> str:
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

    def celsius_to_fahrenheit(self, celsius: int) -> float:
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit: int) -> float:
        return (fahrenheit - 32) / 9 / 5

    def get_primes(self, numbers):
        pass
