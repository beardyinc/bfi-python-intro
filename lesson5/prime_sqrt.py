import math


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


print(is_prime(11))
print(is_prime(23))
print(is_prime(56))
print(is_prime(6574576))
print(is_prime(5694583574))
print(is_prime(23))
