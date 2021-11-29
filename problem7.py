from primes import isPrime, nextPrime

def getNthPrime(n):
    primesFound = 1
    currentPrime = 2
    while primesFound < n:
        currentPrime = nextPrime(currentPrime)
        primesFound = primesFound + 1
    return currentPrime

print getNthPrime(10001)