from primes import isPrime, nextPrime

def getPrimeFactors(n):
    return filter(lambda x: (isPrime(x) and n % x == 0), range(2, n+1))

def getCounts(n):
    primesCount = dict()
    primeFactorsPerNumber = map(getPrimeFactors, range(1,n))
    return primeFactorsPerNumber

print getCounts(20)
# not finished, solved on whiteboard