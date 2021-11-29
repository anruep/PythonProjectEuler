from math import pow
from PyFun.commons import pipe, partial

getSumOfFifthPoweredDigits = pipe(
    str,
    list,
    partial(map,int),
    partial(map(lambda x: math.pow(x, 5)))
    partial(reduce, lambda x,y: x+y)
);

solve = pipe(
    lambda x: [i for i in range(x)],
    filter(lambda a: partial((lambda x,y: x == y), a, getSumOfFifthPoweredDigits(a)),
    partial(reduce, lambda x,y: x+y)
)

print(solve(999999))