from PyFun.commons import partial, pipe

def isDividableByThreeOrFive(x):
    return (x % 3 == 0 or x % 5 == 0)


solve = pipe(
    lambda x: [i for i in range(x)],
    partial(filter, isDividableByThreeOrFive),
    sum
)

print solve(1000)