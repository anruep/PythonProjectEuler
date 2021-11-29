#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

from primes import nextPrime

def getLargestPrimefactor(n):
    prime = 1
    number = n
    while number > 1:
        prime = nextPrime(prime)
        while number % prime == 0:
            number = number / prime
    return prime

print getLargestPrimefactor(600851475143)