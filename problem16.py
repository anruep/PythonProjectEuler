from PyFun.commons import pipe, partial

power2sum = pipe(
    lambda x: 2**x,
    str,
    list,
    partial(map, int),
    sum
)

print power2sum(1000)