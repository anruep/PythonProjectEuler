from math import sqrt, ceil

def isPrime(p):
    if (p == 2 or p == 3):
        return True
    if p % 2 == 0:
        return False
    return len(filter(lambda x: p % x == 0, [i for i in range(1, int(ceil(sqrt(p))) + 1, 2)])) == 1

def nextPrime(p):
    if p % 2 == 0:
        candidate = p+1
    else:
        candidate = p+2
    while True:
        if isPrime(candidate):
            break;
        candidate = candidate + 2
    return candidate