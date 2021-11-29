from PyFun.commons import pipe, partial
from math import ceil

#### WIP ###

def d(n):
    possible = range(1, int(ceil(n/2))+1)
    divisors = filter(lambda x: n % x == 0, possible)
    return sum(divisors)

getDValues = pipe(
    lambda x: range(1,x),
    partial(map, d)
)

sumPairs = pipe(
    partial(map, sum),
    sum
)

def solve(n):
    dValues = getDValues(n)
    amicables = []
    for i in range(len(dValues)):
        for j in range(i+1, len(dValues)):
            if dValues[i] == j+1 and dValues[j] == i+1:
                amicables.append([i+1, j+1])
    return sumPairs(amicables)

print solve(10000)