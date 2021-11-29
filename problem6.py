from PyFun.commons import flatmap

def multiplyEach(myList, multiplikator):
    return map(lambda x: multiplikator * x, myList)

def solve(n):
    flatMultiplies = flatmap(lambda x: multiplyEach(range(x+1, n+1), x), range(1,n+1))
    return 2* reduce(lambda x, y: x + y, flatMultiplies)
    

print solve(100)