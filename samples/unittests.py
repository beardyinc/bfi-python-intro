import math
import unittest

from binary import to_binary
from factorial import calc_factorial
from primecheck import is_prime
from primeseq2 import get_primes


class TestStringMethods(unittest.TestCase):

    def test_prime(self):
        self.assertTrue(is_prime(11), "11 is indeed a prime number")
        self.assertFalse(is_prime(12), "12 is not a prime number")
        self.assertTrue(is_prime(101), "101 is a prime number")

    def test_factorial(self):
        for n in [0, 5, 10, 50, 100]:
            self.assertEqual(math.factorial(n), calc_factorial(n))

        try:
            calc_factorial(-1)
        except ValueError:
            pass
        else:
            self.fail('negative numbers should raise a ValueError')

        try:
            calc_factorial(0.5)
        except ValueError:
            pass
        else:
            self.fail('negative numbers should raise a ValueError')

    def test_binary(self):
        for n in [0, 5, 10, 1034987345]:
            self.assertEqual(bin(n).replace('0b', ''), to_binary(n))

        try:
            to_binary('asdf')
        except ValueError:
            pass
        else:
            self.fail('negative numbers should raise a ValueError')

        try:
            calc_factorial(6.3345)
        except ValueError:
            pass
        else:
            self.fail('negative numbers should raise a ValueError')

    def test_get_primes(self):
        primes = get_primes(100)
        self.assertEqual(len(primes), 27, "expected 27 prime numbers")


if __name__ == '__main__':
    unittest.main()
