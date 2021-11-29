from PyFun.commons import pipe, partial
from primes import nextPrime
from math import ceil, sqrt

def solve(n):
    prime = 2
    sum = 0
    while prime < n:
        sum = sum + prime
        prime = nextPrime(prime)
    return sum

def doTheNet(n):
    net = [i for i in range(2, n)]
    for i in range(2, int(ceil(sqrt(n))) + 1):
        index = i - 2
        if net[index] == 0:
            continue
        for j in range(index*index, n-2):
            if (index == j or net[j] == 0):
                continue
            if net[j] % net[index] == 0:
                net[j] = 0
    filteredNet = filter(lambda x: x > 0, net)
    return filteredNet

solveWithNet = pipe(
    doTheNet,
    partial(reduce, lambda x,y: x+y)
)

print solveWithNet(2000000)
#print solve(2000000)