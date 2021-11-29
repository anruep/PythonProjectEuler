from PyFun.commons import product, pipe, saveMax, partial
from PyFun.maybe import Maybe

def getDoublets(n, minA):
    maxA = n/2 - 1 if n % 2 == 0 else n/2 
    doubles = []
    for i in range(minA, maxA + 1):
        doubles.append([i, n - i])
    return doubles

def getTriplets(n):
    maxA = n/3 -1
    triplets = []
    for i in range(1, maxA + 1):
        iTriplets = map(lambda x: [i] + x, getDoublets(n-i, i+1))
        triplets = triplets + iTriplets
    return triplets

def isPythagorean(t):
    return t[0]*t[0] + t[1] * t[1] == t[2] * t[2]

solve = pipe(
    getTriplets,
    partial(filter, isPythagorean),
    partial(map, product),
    saveMax
)

print solve(12).getOrElse("Error")
print solve(13).getOrElse("Error")
print solve(30).getOrElse("Error")
print solve(1000).getOrElse("Error")