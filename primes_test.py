import unittest
from primes import isPrime, nextPrime

class TestStringMethods(unittest.TestCase):

    def test_isPrime(self):
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(11))
        self.assertTrue(isPrime(29))
        self.assertFalse(isPrime(4))
        self.assertFalse(isPrime(65))

    def test_nextPrime(self):
        self.assertEquals(nextPrime(2), 3)
        self.assertEquals(nextPrime(3), 5)
        self.assertEquals(nextPrime(5), 7)
        self.assertEquals(nextPrime(7), 11)
        self.assertEquals(nextPrime(11), 13)
        self.assertEquals(nextPrime(13), 17)

if __name__ == '__main__':
    unittest.main()