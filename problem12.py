from math import sqrt

def nextTriangleNumber(current, index):
    return current + index + 1

def factorize(num):
    poss = 1
    values = []
    while poss <= sqrt(num):
        if (num % poss == 0):
            values = values + [poss, num / poss]
        poss = poss +1
    return values

def solve(numDivisors):
    triangleNumber = 1
    triangleIndex = 1
    while len(factorize(triangleNumber)) <= numDivisors:
        triangleNumber = nextTriangleNumber(triangleNumber, triangleIndex)
        triangleIndex = triangleIndex + 1
    return triangleNumber


print factorize(6)
print factorize(10)
print factorize(15)
print factorize(21)

print solve(500)