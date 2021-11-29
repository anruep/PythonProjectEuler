def fib(n, limit):
    a, b = 0, 1;
    for i in range(n):
        if a > limit:
            break
        yield a
        # switch to next even fibonacci number (a)
        a, b = a+2*b, 2*a + 3*b
        

print reduce(lambda x,y: x+y, list(fib(2000, 4000000)));