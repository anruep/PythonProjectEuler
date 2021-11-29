from PyFun.commons import pipe, partial, saveMax
from PyFun.maybe import Maybe

def nextCollatz(n):
    return n/2 if n % 2 == 0 else 3*n + 1

def collatzLength(n):
    length = 1
    collatz = n
    while collatz > 1:
        collatz = nextCollatz(collatz)
        length = length + 1
    return length

calculateCollatzLengths = pipe(
    lambda x: [i for i in range(1, x)],
    partial(map, collatzLength)
)

def solve(n):
    collatzLengths = calculateCollatzLengths(n)
    maxCollatz = saveMax(collatzLengths)
    return maxCollatz.map(lambda x: collatzLengths.index(x) + 1)

print solve(1000000).getOrElse("Error")